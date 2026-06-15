# DOCS_RCVD_ALGS

> This table stores discrete allergies information received from outside sources.

**Primary key:** `DOCUMENT_ID`, `CONTACT_DATE_REAL`, `LINE`  
**Columns:** 31  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `DOCUMENT_ID` | NUMERIC | PK shared | This item stores the Received Document record ID. |
| 2 | `CONTACT_DATE_REAL` | FLOAT | PK | This is a numeric representation of the date of this encounter in your system. The integer portion of the number specifies the date of the encounter. The digits after the decimal point indicate multiple visits on one day. |
| 3 | `LINE` | INTEGER | PK | The line number for the information associated with this contact. Multiple pieces of information can be associated with this contact. |
| 4 | `ALG_REF_ID` | VARCHAR |  | This item stores a unique reference identifier to identify a specific instance of an allergy. |
| 5 | `ALG_SEVERITY_C_NAME` | VARCHAR |  | This item stores the overall allergy severity. |
| 6 | `ALG_DATE_NOTED_DT` | DATETIME |  | This item stores the date when the allergy was noted by the external system. |
| 7 | `ALG_DATE_RESOLVD_DT` | DATETIME |  | This item stores the date of when the allergy was resolved. |
| 8 | `ALG_SRC_LPL_ID` | NUMERIC |  | This item stores the source Problem List record identifier. |
| 9 | `ALG_TYPE_OF_CHNG_C_NAME` | VARCHAR |  | This item stores the type of change being performed on the allergy. |
| 10 | `ALGN_NAME` | VARCHAR |  | This item stores the display name of the allergen as sent by the external source. |
| 11 | `ALGN_ID` | NUMERIC |  | This item stores the Allergen record identifier that maps to the allergen from the external source. |
| 12 | `ALGN_ID_ALLERGEN_NAME` | VARCHAR |  | The name of the allergen record. |
| 13 | `ALG_TYPE` | VARCHAR |  | This item stores the textual allergy type sent by the external source. |
| 14 | `ALG_TYPE_ID_C_NAME` | VARCHAR | org | This item stores the category value which maps to the allergy type sent by the external source. |
| 15 | `ALG_SRC_DXR_CSN` | NUMERIC |  | This item will store the contact serial (CSN) number of the Received Document record that owns the instance of this allergy. |
| 16 | `ALG_DUP_OVRD_LPL_ID` | NUMERIC |  | This item stores the record identifier of the local allergy that this external allergy should be grouped with. |
| 17 | `ALG_LAST_UPD_DTTM` | DATETIME (UTC) |  | This item stores the date and time when the allergy was last updated by the external system. |
| 18 | `ALG_PT_SRC_APP_C_NAME` | VARCHAR | org | If this allergy is a patient-entered allergy (i.e. DXR type = 25), this item stores the application which was used to edit the allergy for the contact (e.g. MyChart or Welcome). If blank, this is assumed to be MyChart. |
| 19 | `ALGRX_TYPE` | VARCHAR |  | This item stores the text value of the allergy reaction type sent by the external source. |
| 20 | `ALGRX_TYPE_ID_C_NAME` | VARCHAR | org | This item stores the category value which maps to the allergy reaction type sent by the external source. |
| 21 | `ALG_DT_NOTED_NF_C_NAME` | VARCHAR |  | This item stores the nullFlavor value from the effectiveTime low node in a received CDA document. |
| 22 | `ALG_DT_RESOLV_NF_C_NAME` | VARCHAR |  | This item stores the nullFlavor value from the effectiveTime high node in a received CDA document. |
| 23 | `ALG_STATE_C_NAME` | VARCHAR |  | This item stores the value from the statusCode node in a received CDA document. This item itself is not the status of the allergy. |
| 24 | `ALG_STATUS_ENTRY_C_NAME` | VARCHAR |  | This item stores the value from the status entryRelationship node in a received CDA document. This item itself is not the status of the allergy. |
| 25 | `ALG_HIST_STATUS_C_NAME` | VARCHAR |  | The item indicates whether the allergy is current or historical. |
| 26 | `ALG_HIST_DATE` | DATETIME |  | This item stores the date that the historical status for this allergy is valid through. After this date, the historical status needs to be rechecked. |
| 27 | `ALG_SRC_WPR_ID` | VARCHAR |  | Stores the Patient Access Accounts ID of the MyChart user who edited the allergy for the contact. |
| 28 | `ALG_CRITICALITY_C_NAME` | VARCHAR | org | This item stores the category value for overall allergy criticality. |
| 29 | `ALG_CRITICALITY_TXT` | VARCHAR |  | This item stores the free text allergy criticality. |
| 30 | `ALG_PAT_ENC_CSN_ID` | NUMERIC | FK→ | Stores the contact serial number (CSN) of the encounter that the allergy was added on. |
| 31 | `ALG_EXT_DATA_FILTER_REASON_C_NAME` | VARCHAR |  | Stores the reason why an allergy should be filtered from the composite record. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `ALG_PAT_ENC_CSN_ID` | [PAT_ENC](PAT_ENC.md) | alias_enc_csn | low |

