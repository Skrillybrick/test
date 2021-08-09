// CHANGE 1: Generate a character from upper, lower, or number sets
const generateChar = (asciiSet, asciiMultiplier) => String.fromCharCode(
  Math.floor(Math.random() * asciiSet) + asciiMultiplier);

// CHANGE 2: declaring symbols outside of function so it's not constantly being declared and thrown away.
const symbols = '!@#$%^&*()_+<>?/.,{}[]';

var generatePassword = function() {
  var generatedPassword = '';

  var passwordLength = window.prompt("How many characters should your password include? Please enter between '8' and '128'");

  passwordLength = parseInt(passwordLength);

  if (passwordLength >= 8 && passwordLength <= 128) {
    // confirm lowercase
    var includeLowercase = window.confirm("Include lowercase letters?");

    // confirm uppercase
    var includeUppercase = window.confirm("Include uppercase letters?");

    // confirm numbers
    var includeNumber = window.confirm("Include numbers?");

    // confirm symbols
    var includeSymbol = window.confirm("Include symbols?");

    // CHANGE 3: Make sure that at least one option is selected, otherwise empty password
    if (includeLowercase || includeUppercase || includeNumber || includeSymbol) {
      /* CHANGE 4: Reverse code so that the for loop is outside, and conditionals inside.
                 We incrememnt var i inside of the ifs instead of in the for instantiation, and
                 verify at each step that i<passwordLength. This is better
                 for scalability, and means we don't have to slice at the end.*/
      for (var i=0; i<passwordLength; i) {
        if (includeLowercase && i<passwordLength) {
          generatedPassword += generateChar(26, 97);
          i++;
        }
        if (includeUppercase && i<passwordLength) {
          generatedPassword += generateChar(26, 65);
          i++;
        }
        if (includeNumber && i<passwordLength) {
          generatedPassword += generateChar(10, 48);
          i++;
        }
        if (includeSymbol && i<passwordLength) {
          generatedPassword += symbols[Math.floor(Math.random() * symbols.length)];
          i++
        }
      }
      return generatedPassword;

    } else {
      return "ERROR: EmptyPassword"
    }
  }
}

// Get references to the #generate element
var generateBtn = document.querySelector("#generate");

// Write password to the #password input
function writePassword() {
  var password = generatePassword();
  var passwordText = document.querySelector("#password");

  passwordText.value = password;
}

// Add event listener to generate button
generateBtn.addEventListener("click", writePassword);