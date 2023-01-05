pipeline {
  agent any 
  stages {
     stage(checkout) {
       steps {
         echo"Hello Good Morning Ganesh!"
       }
     }
  }
}
