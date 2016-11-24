import debug from 'debug';

const DEFAULTS = {
  apikey: ''
};

export class BASE {
  constructor(options) {
    BASE.options = Object.assign({}, DEFAULTS, options);
  }
}

/**
 * getDefer
 * @return {object} deferred
 */
const getDefer = exports.getDefer = () => {
  const deferred = {};
  deferred.promise = new Promise((resolve, reject) => {
    deferred.resolve = resolve;
    deferred.reject = reject;
  });
  return deferred;
};

const escaper = str => encodeURIComponent(str).replace(/\*/g, '%2A').replace(/'/g, '%27').replace(/\(/g, '%28').replace(/\)/g, '%29').replace(/\+/, '%2b');

import request from 'request';

exports.sendRequest = (host, params = {}, {method = 'get', timeout = 5000} = {}) => {
  const deferred = getDefer();
  if (method === 'get') {
    const query = Object.keys(params).sort().map(key => `${escaper(key)}=${escaper(params[key])}`).join('&');
    const url = `${host}?${query}`;
    debug('yunpian:common:url')(url);
    request.get(url, {timeout: parseInt(timeout, 10)}, (err, res) => {
      if (err) {
        deferred.reject(err);
      }
      deferred.resolve(JSON.parse(res.body));
    });
  } else {
    debug('yunpian:common:params')(params);
    request({
      method: method.toUpperCase(),
      url: host,
      headers: [
        {
          name: 'content-type',
          value: 'application/x-www-form-urlencoded'
        }
      ],
      timeout: parseInt(timeout, 10),
      form: params
    }, (err, res) => {
      if (err) {
        deferred.reject(err);
      }
      deferred.resolve(JSON.parse(res.body));
    });
  }
  return deferred.promise;
};
