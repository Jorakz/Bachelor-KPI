import java.util.Collections;
import java.util.ArrayList;
import java.util.Scanner;
import java.io.IOException;
import java.io.File;
import java.io.FileWriter;

public class Container_Spectacle   {
    public ArrayList<Spectacle> Constain = new ArrayList<>();

    public Container_Spectacle(){}
    /**
     * Method of reading data from a file
     * @param name contains the name of the data file
     * @throws WorkException is executed when we receive an error while reading the file
     *
     */
    public void Output(String name) throws WorkException {
        try{
            File file = new File (name);
            Scanner scan_file = new Scanner(file);
            String[] parametrs = scan_file.nextLine().split(",");
            int counter = 1;
            while(scan_file.hasNextLine())
            {
                counter+=1;
                try{
                    String data = scan_file.nextLine();
                    Spectacle spectacle = new ID_Spectacle(data, parametrs);
                    Constain.add(spectacle);

                }
                catch(WorkException Exeption){
                    System.out.print(Exeption.getLocalizedMessage());
                    Exeption.FileError(" ERROR IN READING CSV FILE IN ROW #" + counter);
                }
            }

        }
        catch(IOException Exeption)
        {
            throw new WorkException(Exeption.getLocalizedMessage());
        }

    }

    /**
     * The method of writing data to a json file
     * @param name contains the name of the file to which the data will be written
     * @throws WorkException is executed when we get an error while writing the file
     *
     */
    public void Input_json(String name) throws WorkException {
        try(FileWriter Input_in_file = new FileWriter(name)) {
            String text = "[\n";
            for(int i = 0; i < Constain.size(); i++)
            {
                text = text + " {" + (Constain.get(i).toJson()) + " }";
                if(i != (Constain.size() - 1) )
                    text = text + ",";
                text = text + "\n";
            }
            text += "]";

            Input_in_file.write(text);
            Input_in_file.flush();
        }
        catch(IOException Exeption)
        {
            throw new WorkException(Exeption.getLocalizedMessage());
        }
    }

    /**
     * Method that returns an object representation
     * @return output container name
     */
    @Override
    public String toString() {
        return "Spectacle : { " + Constain + "}";
    }

    /**
     * Method that sorts the container
     * @return returns the sorted container
     */
    public void Sort(){
        Collections.sort(Constain);
    }
}
