// Add your code here

public Difference(int[] elements){
    this.elements = elements;
}

public void computeDifference(){
    this.maximumDifference = -999999;

    for (int i=0;i<elements.length;i++){
        for (int j: elements){
            if (i != Arrays.asList(this.elements).indexOf(j)) {
                int value = elements[i] - j;
                if (value > maximumDifference) maximumDifference = value;
            }
        }

    }
}
