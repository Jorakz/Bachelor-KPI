public class Main {
    public static void main(String[] args) throws WorkException {
        String name = args[0];
        Container_Spectacle Data_spectacle = new Container_Spectacle();
        Data_spectacle.Output(name + ".csv");
        System.out.println(Data_spectacle);
        Data_spectacle.Sort();
        Data_spectacle.Input_json(name + ".json");

    }

}
