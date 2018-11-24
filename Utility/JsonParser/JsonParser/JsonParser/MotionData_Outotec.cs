using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace JsonParser.MotionData_Outotec
{
    public class MotionData_Outotec
    {
        public Data[] data { get; set; }
    }

    public class Data
    {
        public long timestamp { get; set; }
        public Event @event { get;set; }
        public Metadata metadata { get; set; }
    }

    public class Event
    {
        public string variable { get; set; }
        public double[] content { get; set; }
    }

    public class Metadata
    {
        public bool validity { get; set; }
        public long timesmap { get; set; }
    }
}
