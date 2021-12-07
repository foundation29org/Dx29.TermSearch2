using System;
using System.Net;

namespace Sample
{
    class Program
    {
        static void Main(string[] args)
        {
            About();

            Issue();

            //RunSymptoms();
            //RunDiseases();

            //RunBatchLoop();
        }

        static private void Issue()
        {
            SearchDiseases("west syndrome");
            SearchSymptoms("seizures");
            SearchSymptoms("convulsiones", "es");
        }

        private static void RunSymptoms()
        {
            SearchSymptoms("");
            SearchSymptoms("HP:00012");
            SearchSymptoms("HP:0001250");

            SearchSymptoms("seizures");
            SearchSymptoms("convulsiones", "es");

            SearchSymptoms("Cant T");
            SearchSymptoms("Cant Talk");
            SearchSymptoms("cant t");
            SearchSymptoms("cant talk");

            SearchSymptoms("Cara ancha", "Es");

            SearchSymptoms("This disease progresses to other seizure types like myoclonic and partial seizures, psychomotor delay, and ataxia");
        }

        private static void RunDiseases()
        {
            SearchDiseases("", "es");

            SearchDiseases("ORPHA:3");
            SearchDiseases("ORPHA:365");
            SearchDiseases("ORPHA:3", "es");
            SearchDiseases("ORPHA:365", "es");

            SearchDiseases("d", "es");
            SearchDiseases("dra", "es");
            SearchDiseases("drav", "es");
            SearchDiseases("dravet", "es");

            SearchDiseases("sindrome", "es");
            SearchDiseases("sindrome dravet", "es");
            SearchDiseases("síndrome dravet", "es");

            SearchDiseases("epile", "es");

            SearchDiseases("pompe", "en");
            SearchDiseases("pompe", "es");
        }

        private static void RunBatchLoop()
        {
            int fails = 0;
            for (int n = 0; n < 100; n++)
            {
                try
                {
                    Run();
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.Message);
                    fails++;
                }
            }
            Console.WriteLine(fails);
        }

        private static void Run()
        {
            SearchSymptoms("");
            SearchDiseases("");

            SearchSymptoms("seizures");
            SearchSymptoms("convulsiones", "es");

            SearchDiseases("dravet");
            SearchDiseases("dravet", "es");
            SearchDiseases("sindrome dravet", "es");
            SearchDiseases("síndrome dravet", "es");

            SearchDiseases("angelman");
            SearchDiseases("angelman", "es");
            SearchDiseases("sindrome angelman", "es");
            SearchDiseases("síndrome angelman", "es");
        }

        #region About
        private static void About()
        {
            var cli = new WebClient();
            var stopwatch = System.Diagnostics.Stopwatch.StartNew();
            // Begin timer
            var res = cli.DownloadString("http://127.0.0.1:8080/api/v1/about/version");
            // End timer
            stopwatch.Stop();
            Console.WriteLine(res);
            Console.WriteLine(stopwatch.Elapsed.TotalSeconds);
        }
        #endregion

        private static void SearchSymptoms(string query, string lang = "en", int rows = 20)
        {
            var cli = new WebClient();
            var stopwatch = System.Diagnostics.Stopwatch.StartNew();
            var res = cli.DownloadString($"http://127.0.0.1:8080/api/v1/search/symptoms?q={query}&lang={lang}&rows={rows}");
            stopwatch.Stop(); Console.WriteLine(stopwatch.Elapsed.TotalSeconds);
            PrintResults(query, res);
            Console.WriteLine();
        }

        private static void SearchDiseases(string query, string lang = "en", int rows = 20)
        {
            var cli = new WebClient();
            var stopwatch = System.Diagnostics.Stopwatch.StartNew();
            var res = cli.DownloadString($"http://127.0.0.1:8080/api/v1/search/diseases?q={query}&lang={lang}&rows={rows}");
            stopwatch.Stop(); Console.WriteLine(stopwatch.Elapsed.TotalSeconds);
            PrintResults(query, res);
            Console.WriteLine();
        }

        private static void PrintResults(string query, string res)
        {
            Console.WriteLine("QUERY: {0}", query);
            var terms = res.Deserialize<Term[]>();

            //Console.WriteLine(terms.Serialize());

            foreach (var term in terms)
            {
                Console.WriteLine("{0}\t{1}", term.Id, term.Name);
            }
        }
    }
}
