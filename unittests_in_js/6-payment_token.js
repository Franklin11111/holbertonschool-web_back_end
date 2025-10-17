function getPaymentTokenFromAPI(success) {
    if (success) {
      return Promise.resolve({ data: 'Successful response from the API' });
    }
    // Returns undefined when success is false
  }
  
  module.exports = getPaymentTokenFromAPI;