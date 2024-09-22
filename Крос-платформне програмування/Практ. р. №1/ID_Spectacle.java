public class ID_Spectacle extends Spectacle {
    private static int id_static = 0;
    private int id = 0;
    public ID_Spectacle() {
        this.id = ++id_static;
    }
    /**
     * A constructor that will receive data from a deadline
     * @param parametrs a string containing data from
     * @param value an array of parameter fields
     * @throws WorkException returns a message if there is an error in the parameters
     */
    public ID_Spectacle(String parametrs, String[] value) throws WorkException {
        super(parametrs,value);
        this.id = ++id_static;
    }
    public int GET_id() {
        return id;
    }

    /**
     * The method of returning the line number to the console
     * @return returns the line number to the console during compilation
     */
    @Override
    public String toString() {

        return "{ID: " + GET_id() +", "+ super.toString()+"}\n";
    }
    /**
     * The method of returning the term number to the Json file
     * @return returns to the console the line number in the Json file
     */
    @Override
    public String toJson(){
        return ("\"ID\": " + id + ", " + super.toJson());
    }





}
