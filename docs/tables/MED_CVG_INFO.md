# MED_CVG_INFO

> This table holds information about medication coverage records.

**Primary key:** `MED_ESTIMATE_ID`  
**Columns:** 16  
**Joined by:** 14 columns

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `MED_ESTIMATE_ID` | NUMERIC | PK | The unique identifier (.1 item) for the medication estimate record. |
| 2 | `CM_PHY_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance that owns this record or line. This is only populated if you use IntraConnect. |
| 3 | `CM_LOG_OWNER_ID` | VARCHAR |  | The Community ID (CID) of the instance from which this record or line was extracted. This is only populated if you use IntraConnect. |
| 4 | `RECORD_CREATION_DATE` | DATETIME |  | Stores the date the record was created. |
| 5 | `CNCT_TYPE_C_NAME` | VARCHAR |  | Stores the record type for this medication estimate. |
| 6 | `CVG_MEMBER_ID` | VARCHAR |  | This holds the member ID associated with this medication estimate. |
| 7 | `PAT_ID` | VARCHAR | FK→ | The unique ID of the patient record for this row (EPT ID). This column is frequently used to link to the PATIENT table. |
| 8 | `ENC_CSN` | NUMERIC |  | Encounter contact serial number of the patient encounter record for this row (EPT CSN). A unique contact serial number in decimal format. |
| 9 | `EPRESCRIBING_NET_ID` | NUMERIC |  | The identifier of the e-prescribing network (DXO) record used for real-time prescription benefits (RTPB) for this estimate. |
| 10 | `EPRESCRIBING_NET_ID_EXTERNAL_NAME` | VARCHAR |  | Organization's external name used as the display name on forms and user interfaces. |
| 11 | `CVG_PAYER_IDNT` | VARCHAR |  | This holds the external ID of the payer associated with this estimate. |
| 12 | `ORDER_ID` | NUMERIC | shared | This item holds the record ID of the order (ORD) this medication estimate is linked to. It may be null if an order has not been linked yet. |
| 13 | `REPORTING_VERSION` | INTEGER |  | This item is used for reporting purposes. It holds a number that is used to determine which items were available when this record was created. |
| 14 | `VIEWED_BEFORE_SIGN_YN` | VARCHAR |  | This item records if a user viewed estimate data in the RTPB window prior to the order being signed. It will only be set to Yes if the the query results were actually displayed prior to signing. This item is only populated on records of type 1-Medication Estimate. |
| 15 | `ALT_VIEWED_BEFORE_SIGN_YN` | VARCHAR |  | This item records if a user ever viewed an alternative in the RTPB window prior to the order being signed. To determine which specific alternatives were viewed, see LME 320-Displayed to User Before Signing. This item is only populated on records of type 1-Medication Estimate. |
| 16 | `RECENT_CONTACT_DATE_REAL` | NUMERIC |  | Returns the most recent contact DTE from Contact Date [I LME 20]. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joins out — this table references

| Column | → References | Method | Confidence |
|--------|--------------|--------|------------|
| `PAT_ID` | [PATIENT](PATIENT.md) | overflow_master | medium |

## Joined in — referenced by (14)

| From | Column | Confidence |
|------|--------|------------|
| [MED_CVG_ALERTS](MED_CVG_ALERTS.md) | `MED_ESTIMATE_ID` | high |
| [MED_CVG_ALERTS_DETAILS](MED_CVG_ALERTS_DETAILS.md) | `MED_ESTIMATE_ID` | high |
| [MED_CVG_ALERTS_TEXT](MED_CVG_ALERTS_TEXT.md) | `MED_ESTIMATE_ID` | high |
| [MED_CVG_ALTERNATIVES](MED_CVG_ALTERNATIVES.md) | `MED_ESTIMATE_ID` | high |
| [MED_CVG_DETAILS](MED_CVG_DETAILS.md) | `MED_ESTIMATE_ID` | high |
| [MED_CVG_DX_VALUE](MED_CVG_DX_VALUE.md) | `MED_ESTIMATE_ID` | high |
| [MED_CVG_ESTIMATE_VALS](MED_CVG_ESTIMATE_VALS.md) | `MED_ESTIMATE_ID` | high |
| [MED_CVG_EVENTS](MED_CVG_EVENTS.md) | `MED_ESTIMATE_ID` | high |
| [MED_CVG_ORD_PA_UPD_HX](MED_CVG_ORD_PA_UPD_HX.md) | `MED_ESTIMATE_ID` | high |
| [MED_CVG_PAYER_INFO](MED_CVG_PAYER_INFO.md) | `MED_ESTIMATE_ID` | high |
| [MED_CVG_RESPONSE_RSLT](MED_CVG_RESPONSE_RSLT.md) | `MED_ESTIMATE_ID` | high |
| [MED_CVG_RESP_RSLT_DETAIL](MED_CVG_RESP_RSLT_DETAIL.md) | `MED_ESTIMATE_ID` | high |
| [MED_CVG_STATUS_DETAILS](MED_CVG_STATUS_DETAILS.md) | `MED_ESTIMATE_ID` | high |
| [MED_CVG_USERACTION](MED_CVG_USERACTION.md) | `MED_ESTIMATE_ID` | high |

