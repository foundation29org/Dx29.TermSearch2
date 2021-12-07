using System;
using System.Collections.Generic;

namespace Sample
{
    public class Term
    {
        public string Id { get; set; }
        public string Name { get; set; }
        public string Desc { get; set; }
        public IList<string> Synonyms { get; set; }
    }
}
