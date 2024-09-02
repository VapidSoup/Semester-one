fetch("./usualsuspects.json")
  .then((response) => response.json())
  .then((Suspects) => {
    console.log(Suspects);
    Suspects.forEach((person) => {
      lineUp(person);
    });
  })
  .catch((error) => {
    console.error(error);
  });

function lineUp(person) {
  switch (person.position) {
    case "Lockpick":
      console.log(
        `${person.fname}, ${person.position} & that's all he is, a lousy lockpick.`
      );
      break;
    case "Demolitions":
      console.log(
        `${person.fname}, ${person.position} might've had something to do with the explosions, but thats it.`
      );
      break;
    case "Theif":
      console.log(
        `${person.fname} ${person.position}... there's probably a plethera of reasons as to why this one died.`
      );
      break;
    case "Ringleader":
      console.log(
        `${person.fname}, ${person.position} is the real Keyser Söze. I know it is. `
      );
      break;
    default:
      console.log(
        `${person.fname}, ${person.position} is the only lead we got, but he's been helpful with these usual suspects.`
      );
      break;
  }
}
