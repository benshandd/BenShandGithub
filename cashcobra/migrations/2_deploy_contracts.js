const CobraCash = artifacts.require('CobraCash.sol');

module.exports = function (deployer) {
  deployer.deploy(CobraCash);
};
