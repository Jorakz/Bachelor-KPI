import java.text.SimpleDateFormat;
import java.util.Date;
public class Spectacle implements Comparable<Spectacle> {
    private String piece_name;
    private String author;
    private String theatre;
    private Date performance_date;
    private int act_quantity;
    private float prise_ticket;
    private boolean music;
    private static final String[] spectacle_field = {"Name","Author","Theatre","Performance_Date","Quantity_of_acts","Ticket_price","Music"};
    private int[] spectacle_order = new int[spectacle_field.length];

    /**
     * Констурктор Spectacle по замовчуванню
     */
    public Spectacle(){

    }

    /**
     * A constructor that stores data and noire from the term
     * @param parameters comma-separated string of data
     * @param value array with name fields order
     * @throws WorkException returns when fields size is incorrect
     */
    public Spectacle(String parameters,String[] value) throws WorkException
    {
        if(parameters == null)
            throw new WorkException(" EMPTY PARAMETERS\n");

        String[] parameter = parameters.split(",");
        if(value.length != 7 || parameter.length != 7)
        {
            throw new WorkException(" INCORRECT QUANTITY OF DATA\n");
        }

        SET_spectacle_data(value);

        SET_piece_name(parameter[spectacle_order[0]]);

        SET_author(parameter[spectacle_order[1]]);

        SET_theatre(parameter[spectacle_order[2]]);

        SET_performance_date(parameter[spectacle_order[3]]);

        SET_act_quantity(parameter[spectacle_order[4]]);

        SET_prise_ticket(parameter[spectacle_order[5]]);

        SET_music(parameter[spectacle_order[6]]);


    }

    /**
     * Method appointment order of fields
     * @param value array with name fields order
     * @throws WorkException returns when fields size is incorrect
     */
    void SET_spectacle_data(String[] value) throws WorkException{
        for(int i = 0; i < spectacle_field.length; ++i) {
            for(int j = 0; j < spectacle_order.length; ++j) {
                if(spectacle_field[i].equals(value[j])) {
                    spectacle_order[i] = j;
                }

            }
        }
    }

    /**
     * Output setting method
     * @return returns a parameter
     */
    public String GET_piece_name()
    {
        return piece_name;
    }

    /**
     * Input setting method
     * @param piece_name contains the parameter data
     */
    public void SET_piece_name(String piece_name)
    {
        this.piece_name = piece_name;
    }
    /**
     * Output setting method
     * @return returns a parameter author
     */
    public String GET_author()
    {
        return author;
    }
    /**
     * Input setting method
     * @param author contains the parameter data
     */
    public void SET_author(String author)
    {
        this.author = author;
    }
    /**
     * Output setting method
     * @return returns a parameter theatre
     */
    public String GET_theatre()
    {
        return theatre;
    }
    /**
     * Input setting method
     * @param theatre contains the parameter data
     */
    public void SET_theatre(String theatre)
    {
        this.theatre = theatre;
    }
    /**
     * Output setting method
     * @return returns a parameter performance_date
     */
    public Date GET_performance_date()
    {
        return performance_date;
    }

    /**
     * Input setting method
     * @param performance_date contains the parameter data
     * @throws WorkException is thrown if the date was entered incorrectly
     */
    public void SET_performance_date(String performance_date) throws WorkException {
        try {
            SimpleDateFormat form = new SimpleDateFormat("dd/MM/yyyy");

            this.performance_date = form.parse(performance_date);
        }
        catch (java.text.ParseException Exeption)
        {
            throw new WorkException(Exeption.getLocalizedMessage() + " INCORRECT PERFORMANCE DATE\n");
        }
    }
    /**
     * Output setting method
     * @return returns a parameter act_quantity
     */
    public int GET_act_quantity()
    {
        return act_quantity;
    }
    /**
     * Input setting method
     * @param act_quantity contains the parameter data
     * @throws WorkException is thrown if the number was entered incorrectly
     */
    public void SET_act_quantity(String act_quantity) throws WorkException
    {
        try
        {
            this.act_quantity = (Integer.parseInt(act_quantity));
        }
        catch (NumberFormatException Exeption) {
            throw new WorkException(Exeption.getLocalizedMessage() + " INCORRECT ACT QUANTITY: MUST BE A NUMBER\n");
        }
    }
    /**
     * Output setting method
     * @return returns a parameter prise_ticket
     */
    public float GET_prise_ticket()
    {

        return prise_ticket;
    }
    /**
     * Input setting method
     * @param prise_ticket contains the parameter data
     * @throws WorkException is thrown if the number was entered incorrectly
     */
    public void SET_prise_ticket(String prise_ticket) throws WorkException
    {
        try {
            this.prise_ticket = (Float.parseFloat(prise_ticket));
        }
        catch (NumberFormatException Exeption)
        {
            throw new WorkException(Exeption.getLocalizedMessage() + " INCORRECT PRICE OF TICKET: MUST BE A NUMBER\n");
        }

    }
    /**
     * Output setting method
     * @return returns a parameter music
     */
    public boolean GET_music()
    {
        return music;
    }
    public void SET_music(Boolean music)
    {
        this.music = music;
    }
    public void SET_music(String music)
    {
        SET_music(Boolean.parseBoolean(music));

    }

    /**
     *
     * @param S the object to be compared.
     * @return returns the adjusted object
     */
    @Override
    public int compareTo(Spectacle S) {
        int res = this.piece_name.compareTo(S.piece_name);
        if(res == 0)
        {
            Integer temp = this.act_quantity;
            res = temp.compareTo(S.act_quantity);
        }
        return res;
    }

    /**
     * The method returns the string parameters to the console
     * @return returns string parameters
     */
    @Override
    public String toString() {
        return "Name: " + piece_name  +
                ", Author: " + author +
                ", Theatre: " +  theatre+
                ", Performance date: " + performance_date+
                ", Quantity of acts: " +  act_quantity+
                ", Ticket price: " + prise_ticket+
                ", Music: " +  music ;

    }

    /**
     * The method returns the string parameters to write to Json
     * @return returns string parameters
     */
    public String toJson() {
        return ("\"Name\": \'" + piece_name  + '\'' +
                ", \"Author\": \'" + author + '\'' +
                ", \"Theatre\": \'" +  theatre+ '\'' +
                ", \"Performance date\": \'" + performance_date+ '\'' +
                ", \"Quantity of acts\": " +  act_quantity +
                ", \"Ticket price\": " + prise_ticket +
                ", \"Music\": " +  music);

}
}

