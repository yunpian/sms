import fs from 'fs';
const lazyLoad = (service) => (() => require(`./${service}`))().default;
const list = fs.readdirSync(__dirname);

list.forEach((item) => {
  if (fs.statSync(`${__dirname}/${item}`).isDirectory()) {
    exports[item.toUpperCase()] = lazyLoad(item);
  }
});

import phone from 'phone';
exports.phone = (number, location = '') => {
  if (number.indexOf('+') === -1 && location === '') {
    return phone(number, 'CHN').length !== 0;
  }
  return phone(number, location).length !== 0;
};
