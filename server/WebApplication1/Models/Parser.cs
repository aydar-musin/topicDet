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
        public static State LoadState()
        {
            string file_path = WebConfigurationManager.AppSettings["state_file_path"];
            var lines = File.ReadAllLines(file_path);

            State state = new State();
            state.Topics = lines[0];

            List<Photo> photos = new List<Photo>();
            for(int i=1;i<lines.Length;i++)
            {
                var args = lines[i].Split('\t');

                Photo photo = new Photo();
                photo.Id = args[0];
                photo.DateTime = DateTime.Parse(args[1]);
                photo.Text = args[2];
                photo.PhotoUrl = args[3];
                photos.Add(photo);
            }
            state.Photos = photos;

            return state;
        }
    }
}