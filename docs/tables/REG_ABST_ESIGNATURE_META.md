# REG_ABST_ESIGNATURE_META

> Stores data about esignatures on a particular abstraction.

**Primary key:** `REGISTRY_DATA_ID`, `LINE`  
**Columns:** 9  
**Org-specific columns:** 1

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `REGISTRY_DATA_ID` | NUMERIC | PK shared | The unique identifier (.1 item) for the registry data record. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `ESIGNATURE_BLOB_KEY` | VARCHAR |  | The blob key of an image of an esignature. |
| 4 | `ESIGNATURE_SIGNER` | VARCHAR |  | The name displayed & associated with an esignature. This can be a legal, preferred, or specified name. |
| 5 | `ESIG_DUAL_SIGN_DEVC_C_NAME` | VARCHAR | org | Stores the device that captured the esignature |
| 6 | `ESIGN_DEVICE_DATA` | VARCHAR |  | Stores a blob key to the device data, which is metadata sent to us by a particular device while capturing an esignature. |
| 7 | `ESIGN_CAPTURE_INST_DTTM` | DATETIME (UTC) |  | The date and time in UTC when the e-signature was captured. |
| 8 | `ESIG_CAPTUREUSER_ID` | VARCHAR |  | The logged in user when a particular signature was captured |
| 9 | `ESIG_CAPTUREUSER_ID_NAME` | VARCHAR |  | The name of the user record. This name may be hidden. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

