# ORDER_MED_5

> This table enables you to report on medications ordered. This table should be used with ORDER_MED.

**Overflow of:** [ORDER_MED](ORDER_MED.md)  
**Primary key:** `ORDER_ID`  
**Columns:** 58  
**Org-specific columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Flags | Description |
|--:|--------|------|-------|-------------|
| 1 | `ORDER_ID` | NUMERIC | PK shared | The unique identifier for the order record. |
| 2 | `FREE_TXT_SUP_PROV_NAME` | VARCHAR |  | This is the name of the supervising provider. |
| 3 | `FREE_TXT_SUP_PROV_IS_EXT_YN` | VARCHAR |  | This indicates whether the supervising provider comes from an external provider database. |
| 4 | `FREE_TXT_SUP_PROV_DEA` | VARCHAR |  | This is the Drug Enforcement Administration (DEA) number of the supervising provider. |
| 5 | `FREE_TXT_SUP_PROV_NPI` | VARCHAR |  | This is the National Provider Identifier (NPI) of the supervising provider. |
| 6 | `FREE_TXT_SUP_PROV_PHONE` | VARCHAR |  | This is the phone number of the supervising provider. |
| 7 | `FREE_TXT_SUP_PROV_FAX` | VARCHAR |  | This is the fax number of the supervising provider. |
| 8 | `FREE_TXT_SUP_PROV_STREET` | VARCHAR |  | This is the street address of the supervising provider. |
| 9 | `FREE_TXT_SUP_PROV_CITY` | VARCHAR |  | This is the city of the supervising provider. |
| 10 | `FREE_TXT_SUP_PROV_STATE_C_NAME` | VARCHAR | org | This is the state of the supervising provider. |
| 11 | `FREE_TXT_SUP_PROV_ZIP` | VARCHAR |  | This is the zip code of the supervising provider. |
| 12 | `FREE_TXT_SUP_PROV_HOUSE` | VARCHAR |  | This is the house number of the supervising provider for medication instructions. |
| 13 | `FREE_TXT_SUP_PROV_DISTRICT_C_NAME` | VARCHAR | org | This is the district of the supervising provider. |
| 14 | `FREE_TXT_SUP_PROV_COUNTY_C_NAME` | VARCHAR | org | This is the county of the supervising provider. |
| 15 | `FREE_TXT_SUP_PROV_COUNTRY_C_NAME` | VARCHAR | org | This is the country of the supervising provider. |
| 16 | `MLSIG_SIGTYPE_C_NAME` | VARCHAR |  | The multiline sig type category ID for the order record, indicating the relationship between multiple sets of medication instructions, each defined for a discrete period of time. '1' or NULL indicates that the order record only has one set of medication instructions. |
| 17 | `HOME_HEALTH_DUE_COMMENT` | VARCHAR |  | The comments entered about the home health medication due time or the person responsible for home health medication administration. |
| 18 | `HH_RESP_PERS_C_NAME` | VARCHAR | org | The home health responsible person category ID for the order record, indicating the person responsible for administering the medication. |
| 19 | `BASE_MED_ORDER_ID` | NUMERIC |  | The unique identifier for the order record representing a multi-product prescription group, containing this order record and others which represent individual product prescriptions within the group. |
| 20 | `MULTI_PROD_IMS_YN` | VARCHAR |  | Indicates whether the order uses multi-product prescription ordering, which selects multiple products to reach the total ordered dose. 'Y' indicates that the medication uses multi-product prescription ordering. 'N' or NULL indicates that the medication uses single-product prescription ordering. |
| 21 | `PA_DISP_OVERRIDE_YN` | VARCHAR |  | This item indicates if prior authorization should be shown or hidden for this order, regardless of whether other data indicates that PA is needed. |
| 22 | `SELECTED_CRCL_SEX_C_NAME` | VARCHAR | org | The sex assigned at birth category ID for the patient sex used in creatinine clearance (CrCl) calculations. |
| 23 | `RX_TYPE_C_NAME` | VARCHAR |  | Flag used to determine how this prescription should be sent to the Finland prescription center. |
| 24 | `MED_PROVENANCE` | VARCHAR |  | This item stores provenance information about medications from external health record systems. |
| 25 | `PAIN_AGREEMENT_YN` | VARCHAR |  | Stores whether or not there is a pain agreement with the patient effective at the time the order was placed. |
| 26 | `HOME_HEALTH_GIVE_PRN_YN` | VARCHAR |  | Indicates whether the home health medication should be given on an as-needed basis in addition to or in place of scheduled due times. 'Y' indicates that the medication should be given on an as-needed basis. 'N' or NULL indicates that the medication should only be given at scheduled due times. |
| 27 | `NO_RENEW_REASON_C_NAME` | VARCHAR |  | The do not renew reason category ID for the order record. |
| 28 | `ORIG_RX_ORDER_CLASS_C_NAME` | VARCHAR | org | For prescription orders created by the interface, this item holds the order class that was assigned at the time the order was created. |
| 29 | `ORDER_INST_UTC_DTTM` | DATETIME (UTC) |  | The date and time the order was placed in UTC. This is the same as the data in ORDER_MED.ORDER_INST, but in UTC. |
| 30 | `HH_NOT_DAILY_YN` | VARCHAR |  | Indicates whether a home health medication is not taken daily. 'Y' indicates that the home health medication is not taken daily. 'N' or NULL indicates that the home health medication is taken daily. |
| 31 | `CONFIDENTIALITY_FLAG_C_NAME` | VARCHAR |  | The hide from proxies flag category ID for the order record, indicating whether the order should be hidden on medication lists shown to a patient's family or proxies. |
| 32 | `ORDERED_DAYS_SUPPLY_PER_FILL` | INTEGER |  | The calculated minimum days supply of the medication ordered. The value for this item is calculated when the order is signed, or when the order is edited by the pharmacy. |
| 33 | `PAUSE_START_DTTM` | DATETIME (Local) |  | The start instant for the pause period of a medication order. |
| 34 | `PAUSE_END_DTTM` | DATETIME (Local) |  | The end instant for the pause period of a medication order. |
| 35 | `PREVIOUS_INR_DATE` | DATETIME |  | The date of the patient's last INR assessment. |
| 36 | `NEXT_INR_DATE` | DATETIME |  | The next date on which a patient's international normalized ratio (INR) should be assessed. |
| 37 | `USER_SEL_ORDER_TEMPLATE_OTL_ID_ORDER_DESC` | VARCHAR |  | Description of the procedure. |
| 38 | `DISP_RECPNT_NAME` | VARCHAR |  | This item holds the recipient name for the dispatch request. |
| 39 | `DISP_RECPNT_CITY` | VARCHAR |  | This item holds the city for this dispatch request. |
| 40 | `DISP_RECPNT_STATE_C_NAME` | VARCHAR |  | This item holds the state for this dispatch request. |
| 41 | `DISP_RECPNT_ZIP` | VARCHAR |  | This item holds the zip code for this dispatch request. |
| 42 | `DISP_RECPNT_COUNTRY_2_C_NAME` | VARCHAR |  | This item holds the country for this dispatch request. |
| 43 | `DISP_RECPNT_HOUSE` | VARCHAR |  | This item holds the house number for this dispatch request. |
| 44 | `DISP_RECPNT_COUNTY_2_C_NAME` | VARCHAR |  | This item holds the county for this dispatch request. |
| 45 | `DISP_RECPNT_DISTRICT_C_NAME` | VARCHAR |  | This item holds the district for this dispatch request. |
| 46 | `HH_IN_BAG_YN` | VARCHAR |  | Indicates whether a home health medication was marked by a clinician as prepacked in a bag. 'Y' indicates that the medication was prepacked in a bag. 'N' or NULL indicates that the medication was not prepacked in a bag. |
| 47 | `HH_IN_PILL_BOX_YN` | VARCHAR |  | Indicates whether a home health medication was marked by a clinician as dispensed in a pill box. 'Y' indicates that the medication was dispensed in a pill box. 'N' or NULL indicates that the medication was not dispensed in a pill box. |
| 48 | `HH_BAG_START_DATE` | DATETIME |  | The start date of a home health medication prepacked in a bag. |
| 49 | `HH_BAG_END_DATE` | DATETIME |  | The end date of a home health medication prepacked in a bag. |
| 50 | `HH_PILL_START_DATE` | DATETIME |  | The start date of a home health medication dispensed in a pill box. |
| 51 | `HH_PILL_END_DATE` | DATETIME |  | The end date of a home health medication dispensed in a pill box. |
| 52 | `BRAND_SEL_RSN_C_NAME` | VARCHAR |  | The brand selected reason category ID for the order, indicating why the brand medication was selected. This column is blank if the brand product was selected because a user specified the medication should be dispensed as written. |
| 53 | `DISCON_PAT_ENC_DATE_REAL` | NUMERIC |  | The encounter or visit in which the medication was discontinued. |
| 54 | `UNIQUE_ORDER_IDENTIFIER` | VARCHAR |  | Order identifier that is unique for all deployments |
| 55 | `REC_W_MAP_ERX_YN` | VARCHAR |  | Flag that indicates if an ORD row was created in Reconcile Outside Information by a user manually choosing an ERX to match with an unmapped DXR prescription. 'Y' Indicates that an order was manually mapped by a user. 'N' indicates that the order was not manually mapped by a user. NULL indicates that the order was not created in Reconcile Outside Information or the item is not used in the current locale. |
| 56 | `HH_OVERRIDE_DOSE_YN` | VARCHAR |  | Indicates whether the reported dose should be used instead of the prescribed dose for med administration in home health. 'Y' indicates that the reported dose should be used. 'N' or NULL indicates that the prescribed dose should be used. |
| 57 | `HH_IN_BAG_REVIEWED_YN` | VARCHAR |  | Indicates if a clinician has acknowledged that the medication was removed from a prepacked bag. 'Y' indicates that the clinician has acknowledged the warning. 'N' or NULL indicates that the warning is not present or has not been acknowledged. |
| 58 | `HH_DUE_TIMES_REVIEWED_YN` | VARCHAR |  | Indicates if a clinician has acknowledged that the due times are correct. 'Y' indicates that the clinician has acknowledged the warning. 'N' or NULL indicates that the warning is not present or has not been acknowledged. |

_Flags: PK = primary key · org = may contain organization-specific values · discont. = discontinued · FK→ = inferred reference (see below) · shared = generic key, intentionally unresolved._

## Joined in

Inbound joins are tracked on the logical base [ORDER_MED](ORDER_MED.md).

