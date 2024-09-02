fetch("./boats.json")
  .then((response) => response.json())
  .then((auction) => {
    auction.forEach((boats) => {
      console.log(discount(boats));
      console.log(getSize(boats));
      console.log(lightCapacity(boats));
      ///console.log(highCapacity(boats));
    });
  })
  .catch((error) => {
    console.error(error);
  });

function discount(boats) {
  switch (boats.bCondition) {
    case "Slight Damage":
      return `The ${boats.bBrand} ${boats.bType} boat is slightly damaged, so it will come at a discounted starting price. `;
      break;
    case "Perfect":
      return `The ${boats.bBrand} ${boats.bType} boat is perfect, so it will start at a normal starting price. `;
      break;
  }
}

function getSize(boats) {
  switch (boats.bSize) {
    case "Medium":
      return `The ${boats.bBrand} ${boats.bType} boat is all for the fast captains.`;
      break;
    case "Small":
      return `The ${boats.bBrand} ${boats.bType} boat is perfect for the casual boater.`;
      break;
    case "Extra Large":
      return `The ${boats.bBrand} ${boats.bType} boat is the perfect boat for a more luxurious experience.`;
      break;
    case "Large":
      return `The ${boats.bBrand} ${boats.bType} boat is a perfect for the more experieced captain.`;
  }
}

function capacity(boats) {
  return boats.bCapacity < 12000;
}
function lightCapacity(boats) {
  if (capacity(boats) === true) {
    return `The ${boats.bBrand} ${boats.bType} boat is a light capacity boat`;
  } else
    return `The ${boats.bBrand} ${boats.bType} boat is a heavy capacity boat`;
}
