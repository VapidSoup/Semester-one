const MotelCustomer = {
  name: "Dillon Regular",
  birthYear: "1999",
  gender: "Male",
  roomPreferences: ["Non-smoking", " King bed"],
  paymentMethod: "Credit card",
  mailingAddress: {
    street: "111 Main St",
    city: "St. John's",
    state: "NL",
    postalCode: "A1A1A1",
  },
  phoneNumber: "555-123-4567",
  checkInDate: "2023-07-20",
  checkOutDate: "2023-07-25",

  getAge: function () {
    const today = new Date();
    return today.getFullYear() - this.birthYear;
  },

  getDurationOfStay: function () {
    const checkInDate = new Date(this.checkInDate);
    const checkOutDate = new Date(this.checkOutDate);
    const durationInMilliseconds = checkOutDate - checkInDate;
    const durationInDays = durationInMilliseconds / (1000 * 60 * 60 * 24);
    return Math.floor(durationInDays);
  },
};

const stay = MotelCustomer.getDurationOfStay();
const age = MotelCustomer.getAge();
const message = `Hey! My name is ${MotelCustomer.name}, I am ${age}. I am a ${MotelCustomer.gender}. So you can say I'm a bit of a dude. Bit of a king actually. I ordered the ${MotelCustomer.roomPreferences}. I am going to be here for ${stay} days. If you have any more questions about myself or the stay I'll be having, you can reach me at ${MotelCustomer.phoneNumber}.`;
console.log(message);
