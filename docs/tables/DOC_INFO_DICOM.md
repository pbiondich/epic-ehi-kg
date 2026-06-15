# DOC_INFO_DICOM

> Table contains information related to DICOM about a document.

**Primary key:** `DOCUMENT_ID`  
**Columns:** 37

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | VARCHAR | PK shared | The unique identifier (.1 item) for the document record. |
| 2 | `ARCHV_ACCESSION_NUM` | VARCHAR |  | The accession number of the imaging study, as pulled from the DICOM image archive (attribute 0008,0050). |
| 3 | `STUDY_INST_UID` | VARCHAR |  | DICOM Study Instance UID (attribute 0020,000D). |
| 4 | `STUDY_DATE` | DATETIME |  | The date this imaging study was performed (attribute 0008,0020). |
| 5 | `STUDY_DESCRIPTION` | VARCHAR |  | The description of this imaging study (attribute 0008,1030). |
| 6 | `SENDING_AE_TITLE` | VARCHAR |  | The title of the sending DICOM Application Entity. |
| 7 | `BELONGS_TO_STUDY_DOCUMENT_ID` | VARCHAR |  | This column stores the ID of the study that this series belongs to. |
| 8 | `MODALITY` | VARCHAR |  | This is the DICOM modality type, as pulled from a DICOM image header (attribute 0008,0060). |
| 9 | `REFERRING_PROV` | VARCHAR |  | Referring physician as per DICOM attributes (attribute 0008,0090). |
| 10 | `SERIES_TM` | DATETIME (Local) |  | The series time per the DICOM attributes (attribute 0008,0031). |
| 11 | `SERIES_DESC` | VARCHAR |  | The series description as per the DICOM attributes (attribute 0008,103E). |
| 12 | `BODY_PART_EXAMINED` | VARCHAR |  | This column stores the body part examined as per the DICOM attribute header (attribute 0018,0015). |
| 13 | `ACQUISITION_TM` | DATETIME (UTC) |  | This column stores the acquisition time of this series (attribute 0008,0032). |
| 14 | `SERIES_LATERALITY` | VARCHAR |  | The DICOM laterality for this series (attribute 0020,0060). |
| 15 | `SERIES_INSTANCE_UID` | VARCHAR |  | The series instance UID for this imaging series (attribute 0020,000E). |
| 16 | `BELONGS_TO_SERIES_DOCUMENT_ID` | VARCHAR |  | This column stores the ID of the series that this image belongs to. |
| 17 | `PRIMARY_IMAGE_INST_UID` | VARCHAR |  | This is the DICOM SOP instance UID (attribute 0008,0018). If this is a CT/MR, then it is the SOP instance UID of the first image in the series. |
| 18 | `INST_SOP_CLASS_UID` | VARCHAR |  | The instance SOP class UID specifies the exact type of this image or other DICOM document (attribute 0008,0016). |
| 19 | `RESCALE_INTERCEPT` | INTEGER |  | Rescale intercept value from the DICOM header (attribute 0028,1052). |
| 20 | `RESCALE_SLOPE` | INTEGER |  | Rescale slope value from the DICOM header (attribute 0028,1053). |
| 21 | `RESCALE_TYPE` | VARCHAR |  | Rescale type value from the DICOM header (attribute 0028,1054). |
| 22 | `SAMPLES_PER_PIXEL` | INTEGER |  | Number of samples per pixel (attribute 0028,0002). |
| 23 | `PIXELS_PER_ROW` | INTEGER |  | The number of pixels per row for this image (attribute 0028,0010). |
| 24 | `IMAGE_COLUMNS` | INTEGER |  | The number of columns of this image (attribute 0028,0011). |
| 25 | `BITS_ALLOCATED` | INTEGER |  | Number of bits allocated. This is bits per pixel (attribute 0028,0100). |
| 26 | `BITS_STORED` | INTEGER |  | The number of bits stored in pixels (attribute 0028,0101). |
| 27 | `PIXEL_SPACING_X_DIR` | NUMERIC |  | Pixel spacing in X direction. This is the first piece of the DICOM attribute (attribute 0028,0030). |
| 28 | `PIXEL_SPACING_Y_DIR` | NUMERIC |  | Pixel spacing in Y direction. This is the second piece of the DICOM attribute (attribute 0028,0030). |
| 29 | `PHOTOMETRIC_INTERPRT` | VARCHAR |  | Photometric interpretation as per the DICOM header (attribute 0028,0004). |
| 30 | `IMAGE_TYPE_C_NAME` | VARCHAR |  | The image type. A multi-frame image is (usually) a movie type image. |
| 31 | `NUM_OF_FRAMES` | INTEGER |  | The number of frames in this image (attribute 0028,0008). |
| 32 | `MAX_PIX_VALUE` | INTEGER |  | This is the maximum pixel value in this image. This value is used to determine usable window width and level adjustment ranges. |
| 33 | `FRAME_TM` | NUMERIC |  | This column stores the frame time as time between image frames in milliseconds and it is used for setting initial display speeds. |
| 34 | `IMAGE_ORIENTATION` | VARCHAR |  | Image orientation defines the spatial position of the patient in relation to the image (derived from attribute 0020,0037). |
| 35 | `PAT_ORIENTATION` | VARCHAR |  | The patient orientation defines the patient position in relation to the image (attribute 0020, 0020). |
| 36 | `SLICE_THICKNESS` | VARCHAR |  | This column stores the slice thickness of the image. This is only relevant for cross-sectional images (attribute 0018,0050). |
| 37 | `IMAGE_LOCATION` | VARCHAR |  | This column stores a URL that can be used to retrieve this image through a WADO-RS web service call. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

