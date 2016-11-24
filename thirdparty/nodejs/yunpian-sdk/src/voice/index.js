import {BASE, sendRequest} from '../common';
import ACTIONS from './list';
const API = 'https://voice.yunpian.com/v2/voice/';

export default class Voice extends BASE {
  constructor(options, acts = Object.keys(ACTIONS)) {
    super(options);
    const actions = typeof acts === 'string' ? [acts] : acts;
    actions.forEach(action => {
      this[action] = this[action.replace(/(\w)/, v => v.toLowerCase())] = async(opts, to) => {
        this.params = Object.assign(BASE.options, opts);
        return sendRequest(`${API}${ACTIONS[action].action}.json`, this.params, {method: ACTIONS[action].method, timeout: to});
      };
    });
  }
}
