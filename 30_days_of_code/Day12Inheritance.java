class Student extends Person{
	private int[] testScores;

    public Student(String firstName, String lastName, int identification, int[] testScores){
        super(firstName, lastName, identification);
        this.testScores = testScores;
    }

    public char calculate(){
        char rtn = 'K';
        int sum = 0;
        for (int score: testScores){
            sum += score;
        }
        int avg = sum/testScores.length;

        if (90 <= avg && avg <= 100){
                rtn = 'O';
        } else if (80 <= avg && avg <= 90){
            rtn = 'E';
        } else if (70 <= avg && avg <= 80){
            rtn = 'A';
        } else if (55 <= avg && avg <= 70){
            rtn = 'P';
        } else if (40 <= avg && avg <= 55){
            rtn = 'D';
        } else if (avg <= 40){
            rtn = 'T';
        }
        return rtn;
    }

}
