using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace JsonParser
{
    class Program
    {
        private const string PathToWav = @"C:\hackjunction18\IHearVoicesData\Audio";
        private const string PathToJson = @"C:\hackjunction18\IHearVoicesData\Motion";
        private const string PathToCsvSALT = @"C:\hackjunction18\IHearVoicesData\Motion\CSV\dataSALT.csv";
        private const string PathToCsvPEPA = @"C:\hackjunction18\IHearVoicesData\Motion\CSV\dataPEPA.csv";

        static void Main(string[] args)
        {
            //LookUpDataFiles();

            //20181025_1100.json -- sensor blew up

            var timeFrom = new DateTimeOffset(new DateTime(2018, 10, 22, 00, 00, 00, DateTimeKind.Utc));
            var timeTo = new DateTimeOffset(new DateTime(2020, 10, 21, 23, 59, 0, DateTimeKind.Utc));

            var jsonList = GetJsonList(timeFrom, timeTo);

            var allDataLinesSALT = new StringBuilder();
            var allDataLinesPEPA = new StringBuilder();

            foreach (var json in jsonList)
            {
                var reduced = ParseMotionData(json);

                foreach (var point in reduced.data)
                {
                    var line = string.Join("😈", point.content.Select(_ => _.ToString()));
                    line = string.Join("😈", point.timestamp.ToString(), line);
                    switch (point.variable)
                    {
                        case "SALT-quaternion":
                        case "SALT-acceleration":
                            allDataLinesSALT.AppendLine(line);
                            break;
                        case "PEPA-quaternion":
                        case "PEPA-acceleration":
                            allDataLinesPEPA.AppendLine(line);
                            break;
                    }
                }

                var index = jsonList.IndexOf(json) + 1;
                Console.WriteLine($"{index} of {jsonList.Count}    ({(((float)index)*100/(float)jsonList.Count).ToString("0.00")}%)");

                File.AppendAllText(PathToCsvSALT, allDataLinesSALT.ToString());
                File.AppendAllText(PathToCsvPEPA, allDataLinesPEPA.ToString());

                allDataLinesPEPA.Clear();
                allDataLinesSALT.Clear();
            }
        }

        private static void LookUpDataFiles()
        {
            var timeFrom = new DateTimeOffset(new DateTime(2018, 10, 12, 14, 35, 0, DateTimeKind.Utc));
            var timeTo = new DateTimeOffset(new DateTime(2018, 10, 15, 20, 35, 0, DateTimeKind.Utc));

            var wavList = GetWavList(timeFrom, timeTo);
            var jsonList = GetJsonList(timeFrom, timeTo);
        }

        private static List<string> GetJsonList(DateTimeOffset timeFrom, DateTimeOffset timeTo)
        {
            var listOfJsonOrig = System.IO.Directory.EnumerateFiles(PathToJson).ToList();
            var listOfJson = listOfJsonOrig.Select(j => JsonFileNameToDateTimeString(j)).ToList();
            var listOfJsonEpoch = listOfJson.Select(j => DateTimeStringToEpoch(j));

            var result = new List<string>();

            var jsonFrom = GetJsonByEpoch(listOfJsonEpoch, timeFrom.ToUnixTimeMilliseconds());
            var jsonTo = GetJsonByEpoch(listOfJsonEpoch, timeTo.ToUnixTimeMilliseconds());

            var jsonFromIndex = listOfJsonOrig.IndexOf(jsonFrom);
            var jsonToIndex = listOfJsonOrig.IndexOf(jsonTo);

            result.AddRange(listOfJsonOrig.GetRange(jsonFromIndex, jsonToIndex - jsonFromIndex + 1));

            return result;
        }

        private static string GetJsonByEpoch(IEnumerable<long> listOfJsonEpoch, long v)
        {
            var closestNeighbour = (listOfJsonEpoch.Where(e => e - v <= 0).Reverse()).Count()<1 ? listOfJsonEpoch.First() : (listOfJsonEpoch.Where(e => e - v <= 0).Reverse()).First();

            var distance = closestNeighbour - v;

            var jsonPath = EpochToJsonFileName(closestNeighbour);

            bool exists = System.IO.File.Exists(jsonPath);
            return jsonPath;
        }

        private static string EpochToJsonFileName(long closestNeighbour)
        {
            return DateTimeStringToJsonFileName(DateTimeOffset.FromUnixTimeMilliseconds(closestNeighbour));
        }

        private static string DateTimeStringToJsonFileName(DateTimeOffset date)
        {
            var json = string.Empty;

            //20181012_1500
            var year = date.Year;
            var month = date.Month;
            var day = date.Day;
            var hour = date.Hour;
            var minute = date.Minute;

            json = string.Concat(PathToJson, @"\", year.ToString("0000"), month.ToString("00"), day.ToString("00"),"_", hour.ToString("00"), minute.ToString("00"), ".json");
            return json;
        }

        private static string JsonFileNameToDateTimeString(string j)
        {
            //20181012_1500
            var json = j.Substring(PathToJson.Length + 1, 13);

            var year = json.Substring(0, 4);
            var month = json.Substring(4, 2);
            var day = json.Substring(6, 2);
            var hour = json.Substring(9, 2);
            var minutes = json.Substring(11, 2);
            var seconds = "00";
            var miliseconds = "000";

            json = string.Concat(year, "-", month, "-", day, "T", hour, ":", minutes, ":", seconds, ".", miliseconds, "Z");

            return json;
        }

        private static List<string> GetWavList(DateTimeOffset timeFrom, DateTimeOffset timeTo)
        {
            var listOfWavOrig = System.IO.Directory.EnumerateFiles(PathToWav).ToList();
            var listOfWav = listOfWavOrig.Select(w => WavFileNameToDateTimeString(w)).ToList();

            var listOfWaveEpoch = listOfWav.Select(w => DateTimeStringToEpoch(w));

            var result = new List<string>();

            var wavFrom = GetWavByEpoch(listOfWaveEpoch, timeFrom.ToUnixTimeMilliseconds());
            var wavTo = GetWavByEpoch(listOfWaveEpoch, timeTo.ToUnixTimeMilliseconds());

            var wavFromIndex = listOfWavOrig.IndexOf(wavFrom);
            var wavToIndex = listOfWavOrig.IndexOf(wavTo);

            result.AddRange(listOfWavOrig.GetRange(wavFromIndex, wavToIndex - wavFromIndex + 1));

            return result;
        }

        private static string GetWavByEpoch(IEnumerable<long> listOfWaveEpoch, long motionPoint)
        {
            var closestNeighbour = listOfWaveEpoch.Where(e => e - motionPoint <= 0).Reverse().First();

            var distance = closestNeighbour - motionPoint;

            var wavPath = EpochToWavFileName(closestNeighbour);

            bool exists = System.IO.File.Exists(wavPath);
            return wavPath;
        }

        private static long DateTimeStringToEpoch(string w)
        {
            return System.Xml.XmlConvert.ToDateTimeOffset(w).ToUnixTimeMilliseconds();
        }

        private static string EpochToWavFileName(long w)
        {
            return DateTimeStringToWavFileName(DateTimeOffset.FromUnixTimeMilliseconds(w));
        }

        private static string DateTimeStringToWavFileName(DateTimeOffset wav)
        {
            var year = wav.Year;
            var month = wav.Month;
            var day = wav.Day;
            var hour = wav.Hour;
            var minutes = wav.Minute;
            var seconds = wav.Second;
            var miliseconds = wav.Millisecond;

            var wave = string.Concat(
                PathToWav,
                @"\device1_channel1_",
                year.ToString("0000"),
                month.ToString("00"),
                day.ToString("00"),
                hour.ToString("00"),
                minutes.ToString("00"),
                seconds.ToString("00"),
                ".wav");

            return wave;
        }

        private static string WavFileNameToDateTimeString(string wav)
        {
            var wave = wav.Substring(PathToWav.Length + 18, 14);

            var year = wave.Substring(0, 4);
            var month = wave.Substring(4, 2);
            var day = wave.Substring(6, 2);
            var hour = wave.Substring(8, 2);
            var minutes = wave.Substring(10, 2);
            var seconds = wave.Substring(12, 2);
            var miliseconds = "000";

            wave = string.Concat(year, "-", month, "-", day, "T", hour, ":", minutes, ":", seconds, ".", miliseconds,"Z");

            return wave;
        }

        private static MotionData_Reduced.MotionData_Reduced ParseMotionData(string path)
        {
            var motionDataFile = System.IO.File.ReadAllText(path);

            var motionData = Newtonsoft.Json.JsonConvert.DeserializeObject<MotionData_Outotec.MotionData_Outotec>(motionDataFile);
            //var metadata = motionData.data.Any(d => d.metadata == null);
            //var validity = motionData.data.Any(d => d.metadata?.validity != true);



            return new MotionData_Reduced.MotionData_Reduced(motionData);
        }
    }
}