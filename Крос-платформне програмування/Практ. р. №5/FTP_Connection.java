import org.apache.commons.net.ftp.*;
import org.apache.commons.net.ftp.FTPClient;
import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;
import java.io.File;
import java.io.FileOutputStream;

public class FTP_Connection {
    private final FTPClient FTP_Client;
    private FTPFile[] FTP_Files;

    public FTP_Connection(String url, int port, String username, String password) throws IOException {
        FTP_Client = new FTPClient();
        FTP_Client.connect(url, port);
        FTP_Client.login(username, password);
        FTP_Client.enterLocalPassiveMode();
    }
    public List<String> GET_file_names(String dir) throws IOException {
        this.SET_ftp_files(dir);
        return Arrays.stream(FTP_Files).map(FTPFile::getName).collect(Collectors.toList());
    }

    public void SET_ftp_files(String dir) throws IOException {
        this.FTP_Files = FTP_Client.listFiles(dir);
    }

    public void DOWNLOAD_file(String fileName, String localDir, String remoteDir) throws IOException
    {
        for (FTPFile ftpFile: FTP_Files) {
            if (ftpFile.getName().equals(fileName)) {
                new File(localDir).mkdirs();
                File file = new File(localDir + "/" + fileName);
                file.createNewFile();
                FileOutputStream fos = new FileOutputStream(localDir + "/" + fileName, false);
                FTP_Client.retrieveFile(remoteDir+ "/" +fileName, fos);
                return;
            }
        }

    }
}