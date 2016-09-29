public class Person {
    private int age;

	public Person(int initialAge) {
  		// Add some more code to run some checks on initialAge
        if (initialAge < 0) {
            System.out.println("Age is not valid, setting age to 0.");
            this.age = 0;
        } else {
            this.age = initialAge;
        }
	}

	public void amIOld() {
        String message;
        if (this.age < 13) {
            message = "You are young.";
        } else if (this.age >= 13 && this.age < 18) {
            message = "You are a teenager.";
        } else {
            message = "You are old.";
        }
        System.out.println(message);
	}

	public void yearPasses() {
  		// Increment this person's age.
        this.age+=1;
	}
