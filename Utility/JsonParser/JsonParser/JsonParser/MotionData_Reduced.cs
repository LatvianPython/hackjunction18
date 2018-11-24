using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using JsonParser.MotionData_Outotec;

namespace JsonParser.MotionData_Reduced
{
    public class MotionData_Reduced
    {
        public MotionData_Reduced(MotionData_Outotec.MotionData_Outotec motionData)
        {
            this.data = motionData.data.Select(d =>
                new Data
                {
                    content = d.@event.content.Take(d.@event.content.Length - 1).ToArray(),
                    variable = string.Join("-", d.@event.variable.Substring(6, 4), d.@event.variable.Substring(11)),
                    timestamp = d.timestamp,
                }
            ).ToArray();
        }

        public Data[] data { get; set; }
    }

    public class Data
    {
        public long timestamp { get; set; }
        public string variable { get; set; }
        public double[] content { get; set; }     
    }
}
