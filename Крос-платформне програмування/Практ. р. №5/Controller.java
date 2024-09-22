import javafx.application.Platform;
import javafx.embed.swing.SwingFXUtils;
import javafx.fxml.FXML;
import javafx.scene.canvas.Canvas;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ListView;
import javafx.scene.text.Text;
import javafx.scene.image.Image;

import java.io.IOException;
import java.util.*;

public class Controller {

    @FXML
    public Canvas CANVAS_WIDGET;
    @FXML
    public Button DOWNLOAD_button;
    @FXML
    public Button LOOP_button;
    @FXML
    public Label IMAGE_VIEW;
    @FXML
    public Text SHOW_IMAGE_INFO;

    @FXML
    public ListView<String> slices_COLLECT_View;
    private FTP_Connection ftpConnection;
    private DICOMImage_collection dicom_Image_Collect;
    private List<String> FILENAMES;
    private Map<Double, Integer> slices;

    private int CURRENT_Image_ID = 0;
    private List<DICOMImage> CURRENT_Images = new ArrayList<>();

    String local_dir;
    String remote_dir;

    boolean isLoop = false;

    TimerTask timerTask;

    @FXML
    public void initialize(String url, int port, String user, String pass, String localDir, String remoteDir)
            throws IOException {
        LOOP_button.setDisable(true);
        ftpConnection = new FTP_Connection(url, port, user, pass);
        dicom_Image_Collect = new DICOMImage_collection();
        this.local_dir = localDir;
        this.remote_dir = remoteDir;

    }

    @FXML
    public void Download_DICOM() {
        DOWNLOAD_button.setDisable(true);
        try {
            FILENAMES = ftpConnection.GET_file_names(remote_dir);
            var thread = new Thread(new Runnable() {
                String FILENAME;
                int downloadingIndex;

                @Override
                public void run() {
                    Runnable textUpdater = () -> SHOW_IMAGE_INFO.setText(
                            "Завантаження: " + (downloadingIndex + 1) + "/" + FILENAMES.size() + " " + FILENAME );
                    for (int i = 0; i < FILENAMES.size(); i++) {
                        FILENAME = FILENAMES.get(i);
                        downloadingIndex = i;
                        try {
                            ftpConnection.DOWNLOAD_file(FILENAME , local_dir, remote_dir);
                            dicom_Image_Collect.ADD_Image(local_dir, FILENAME );
                            Platform.runLater(textUpdater);
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                    }
                    dicom_Image_Collect.Sort_collections();
                    slices = dicom_Image_Collect.GET_Slices();
                    for (Double sliceLocation : slices.keySet()) {
                        Platform.runLater(() -> slices_COLLECT_View.getItems()
                                .add("Місцезнаходження: " + sliceLocation +", Розмір: " + slices.get(sliceLocation)));
                    }
                    SHOW_IMAGE_INFO.setText("Завантаження файлів завершено!");
                }
            });
            thread.setDaemon(true);
            thread.start();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @FXML
    public void Looping_Slice() {
        if (isLoop) {
            timerTask.cancel();
            LOOP_button.setText("Розпочати цикл");
        } else {
            timerTask = new TimerTask() {
                @Override
                public void run() {
                    Platform.runLater(() -> Show_Current_Image());
                }
            };
            var timer = new Timer(true);
            timer.scheduleAtFixedRate(timerTask, 0, 50);
            LOOP_button.setText("Зупинити цикл");
        }
        isLoop = !isLoop;
    }

    private void Show_Current_Image() {
        DICOMImage dicomImage = CURRENT_Images.get(CURRENT_Image_ID);
        IMAGE_VIEW.setText("Назва: " + dicomImage.FileName + "\nНомер серії: "
                + dicomImage.SeriesNumber + "\nНомер знаття: "
                + dicomImage.AcquNumber + "\nНомер екземпляру: " + dicomImage.InstNumber);

        Image image = SwingFXUtils.toFXImage(dicomImage.Image, null);
        var ctx = CANVAS_WIDGET.getGraphicsContext2D();
        CANVAS_WIDGET.setWidth(image.getWidth());
        CANVAS_WIDGET.setHeight(image.getHeight());
        ctx.drawImage(image, 0, 0);

        CURRENT_Image_ID = CURRENT_Image_ID < CURRENT_Images.size() - 1 ? ++CURRENT_Image_ID : 0;
    }

    public void Object_Select() {
        Integer index = slices_COLLECT_View.getSelectionModel().getSelectedIndex();
        CURRENT_Images = dicom_Image_Collect.GET_Images_Slide((double) slices.keySet().toArray()[index]);
        CURRENT_Image_ID = 0;
        Show_Current_Image();
        if (LOOP_button.isDisable())
            LOOP_button.setDisable(false);

    }
}