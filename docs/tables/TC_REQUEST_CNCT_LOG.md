# TC_REQUEST_CNCT_LOG

> This table stores information about the contacts associated with Transfer Center requests.

**Primary key:** `COMM_ID`, `LINE`  
**Columns:** 10  
**Org-specific columns:** 2

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `COMM_ID` | NUMERIC | PK shared | The unique identifier for the Transfer Center request. |
| 2 | `LINE` | INTEGER | PK | The line number for the information associated with this record. Multiple pieces of information can be associated with this record. |
| 3 | `CONTACT_PROV_ID_PROV_NAME` | VARCHAR |  | The name of the service provider. This item may be hidden in a public view of the CLARITY_SER table. |
| 4 | `CONTACT_ROLE_C_NAME` | VARCHAR | org | This item stores the role of a contact on the contact log. |
| 5 | `CONTACT_NAME` | VARCHAR |  | This item stores the name of the person associated with a given entry in the contact log. |
| 6 | `CONTACT_PH_NUM` | VARCHAR |  | This item stores the phone number for an entry in the contact log. |
| 7 | `CONTACT_LOC_ID_LOC_NAME` | VARCHAR |  | The name of the revenue location. |
| 8 | `FROM_REF_LOC_YN` | VARCHAR |  | This item specifies whether this contact is associated with the referring location of a Transfer Center request. |
| 9 | `CNCT_IS_ADMT_PROV_YN` | VARCHAR |  | Indicates whether the associated contact an admitting provider for a location . 'Y' indicates that they are. 'N' or NULL indicates that they are not the admitting provider. |
| 10 | `CONTACT_HOSP_SERV_C_NAME` | VARCHAR | org | The contact's related service |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

