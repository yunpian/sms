using System;
using System.Collections;
using System.Collections.Generic;
using System.Net.Http;
using System.Text;

namespace YunPian.ApiClient
{
    internal class FormUrlEncodedContentBuilder : IEnumerable
    {
        private readonly List<KeyValuePair<string, string>> _keyValueCollection;

        public FormUrlEncodedContentBuilder()
        {
            _keyValueCollection = new List<KeyValuePair<string, string>>();
        }

        public void Add(string key, string value)
        {
            _keyValueCollection.Add(new KeyValuePair<string, string>(key, value));
        }

        public static implicit operator FormUrlEncodedContent(FormUrlEncodedContentBuilder _this)
        {
            return new FormUrlEncodedContent(_this._keyValueCollection);
        }

        public IEnumerator GetEnumerator()
        {
            return _keyValueCollection.GetEnumerator();
        }
    }
}
