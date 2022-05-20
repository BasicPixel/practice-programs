// https://dev.to/martinkr/array-map-of-occurrences-4ndp

const mapOccurrences = arr => arr.reduce((acc, current) => (acc[current] = (acc[current] || 0) + 1, acc), {}); 
