using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Configuration;
using System.IO;

namespace WebApplication1.Models
{
    public static class Parser
    {
        public static List<Photo> LoadPhotos()
        {
            string file_path = WebConfigurationManager.AppSettings["photos_file_path"];
            var lines = File.ReadAllLines(file_path);

            List<Photo> result = new List<Photo>();

            foreach (var line in lines)
            {
                var args = line.Split('\t');

                Photo photo = new Photo();
                photo.Id = args[0];
                photo.DateTime = DateTime.Parse(args[1]);
                photo.Text = args[2];
                photo.PhotoUrl = args[3];
                result.Add(photo);
            }

            return result;
        }
    }
}