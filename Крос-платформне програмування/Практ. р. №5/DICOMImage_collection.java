import java.util.*;
import java.util.stream.Collectors;

public class DICOMImage_collection {
    public ArrayList<DICOMImage> images = new ArrayList<>();

    private Map<Double, Integer> slices = new HashMap<>();;

    public void ADD_Image(String dir, String fileName) {
        try {
            DICOMImage dicomImage = new DICOMImage(dir, fileName);
            images.add(dicomImage);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
    
    public void Sort_collections() {
        Collections.sort(images);
    }

    public Map<Double, Integer> GET_Slices() {
        if (slices.size() == 0 && images.size() > 0) {
            slices = new HashMap<>();
            images.stream().collect(Collectors.groupingBy(image -> image.SliceLocation)).forEach((k, v) -> slices.put(k, v.size()));
        }
        return slices;
    }

    public List<DICOMImage> GET_Images_Slide(double sliceLocation) {
        return images.stream().filter(i -> i.SliceLocation == sliceLocation).collect(Collectors.toList());
    }
}