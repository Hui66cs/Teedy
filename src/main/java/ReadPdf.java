import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.text.PDFTextStripper;
import java.io.File;

public class ReadPdf {
    public static void main(String[] args) throws Exception {
        PDDocument document = PDDocument.load(new File("/home/zhu/projects/Teedy/Practice8-Coverage.pdf"));
        PDFTextStripper stripper = new PDFTextStripper();
        String text = stripper.getText(document);
        System.out.println(text);
        document.close();
    }
}
