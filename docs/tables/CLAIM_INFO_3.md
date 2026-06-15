# CLAIM_INFO_3

> This table contains claims information from claim information (CLM) records for Hospital and Professional Billing.

**Overflow of:** [CLAIM_INFO](CLAIM_INFO.md)  
**Primary key:** `CLAIM_ID`  
**Columns:** 12  
**Org-specific columns:** 4

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `CLAIM_ID` | NUMERIC | PK | The unique identifier for the Claim Info record. |
| 2 | `STER_ABORTION_CD_C_NAME` | VARCHAR | org | Stores the sterilization/abortion code to print on the claim. |
| 3 | `SVC_AUTH_EXCEPT_C_NAME` | VARCHAR | org | This column stores the service authorization exception code detailing why a claim was exempt from the normal authorization process. |
| 4 | `AMBULANCE_LICENSE_PLATE_NUMBER` | VARCHAR |  | The license plate number of the ambulance used for transport |
| 5 | `AMBULANCE_PICK_UP_UTC_DTTM` | DATETIME (UTC) |  | The pick-up time of the ambulance ride |
| 6 | `AMBULANCE_DROP_OFF_UTC_DTTM` | DATETIME (UTC) |  | The drop-off time of the ambulance ride |
| 7 | `AMBULANCE_ROUNDTRIP_REASON` | VARCHAR |  | The reason for roundtrip for the ambulance ride |
| 8 | `AMBU_STRETCHER_REASON_C_NAME` | VARCHAR | org | The reason for stretcher for the ambulance ride |
| 9 | `AMBULANCE_SQUAD_C_NAME` | VARCHAR | org | The ambulance squad of the ambulance that the patient rode in |
| 10 | `AMBULANCE_RUN_NUMBER` | VARCHAR |  | The run number of the ambulance ride that transported the patient |
| 11 | `AMBULANCE_VEHICLE_NUMBER` | VARCHAR |  | The vehicle number for the ambulance that transported the patient |
| 12 | `AMBULANCE_DISPATCH_DX_ID_DX_NAME` | VARCHAR |  | The name of the diagnosis. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [CLAIM_INFO](CLAIM_INFO.md).

