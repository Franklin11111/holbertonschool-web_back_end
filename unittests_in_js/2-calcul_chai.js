function calculateNumber(type, a, b) {
	const numA = Number(a);
	const numB = Number(b);
  
	if (Number.isNaN(numA) || Number.isNaN(numB)) {
	  throw new TypeError('Invalid input');
	}
  
	if (type === 'SUM') {
	  return Math.round(numA) + Math.round(numB);
	} else if (type === 'SUBTRACT') {
	  return Math.round(numA) - Math.round(numB);
	} else if (type === 'DIVIDE') {
	  if (Math.round(numB) === 0) {
		return 'Error';
	  }
	  return Math.round(numA) / Math.round(numB);
	} else {
	  throw new TypeError('Invalid operation type');
	}
  }
  
  module.exports = calculateNumber; 