using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace WebApplication1.Models
{
    public class Photo
    {
        public string Id { get; set; }
        public DateTime DateTime { get; set; }
        public string PhotoUrl { get; set; }
        public string Text { get; set; }
    }
}