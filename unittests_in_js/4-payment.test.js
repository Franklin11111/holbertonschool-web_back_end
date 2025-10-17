const sinon = require('sinon');
const chai = require('chai');
const expect = chai.expect;
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', () => {
  let calculateNumberStub;
  let consoleSpy;

  beforeEach(() => {
    // Stub Utils.calculateNumber to always return 10
    calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10);
    // Spy on console.log
    consoleSpy = sinon.spy(console, 'log');
  });

  afterEach(() => {
    // Restore the stub and spy after each test
    calculateNumberStub.restore();
    consoleSpy.restore();
  });

  it('should call Utils.calculateNumber with SUM, 100, 20', () => {
    sendPaymentRequestToApi(100, 20);
    
    // Verify the stub was called correctly
    expect(calculateNumberStub.calledOnce).to.be.true;
    expect(calculateNumberStub.calledWith('SUM', 100, 20)).to.be.true;
  });

  it('should log the correct total to console', () => {
    sendPaymentRequestToApi(100, 20);
    
    // Verify console output
    expect(consoleSpy.calledOnce).to.be.true;
    expect(consoleSpy.calledWith('The total is: 10')).to.be.true;
  });
});