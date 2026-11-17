---
title: "AI Training Data Supplier Diligence"
subtitle: "Requirements and Evidence for Buyers of AI Training Data"
version: "Version 0 (v0), public draft for adoption"
author: "Andrew Delaurier Weeks"
credentials: "PCI DSS assessment work, Fortune 500 payment environments; ISO/IEC 27001:2022 Lead Auditor certification"
credentials_full: "PCI DSS assessment work, Fortune 500 payment environments; ISO/IEC 27001:2022 Lead Auditor certification (Mastermind Assurance, 2025); Certificate of Cloud Security Knowledge v5; CompTIA Security+; former security-operations analyst at a financial institution; business-continuity and disaster-recovery practitioner; systems developer in Rust."
capacity_cover: "Written in a personal capacity; not on behalf of, or reviewed by, any employer."
capacity: "Written and published by the author in a personal capacity. No employer or client of the author took part in it, reviewed it, or is bound by it, and no employer of the author has any role in the practice described in Part 6. Reading it forms no engagement and no professional relationship. It is a procurement standard; it contains no legal advice and is no audit, certification or assurance of any result."
title_display: "AI Training Data Supplier Diligence"
serial: "AI-TDSD 0000 0001 A"
date: "2026-11-16"
license: "Text: Creative Commons Attribution 4.0 International. Schema, example and validator (Annex A): MIT License."
---

## 0. How to use this document

This document is written for the people at a laboratory or company who decide a training-data purchase. Two of them sign: counsel and the data-acquisition lead. Two more use parts of it: the evaluation lead and the engineers who run procurement systems.

**Counsel** reads Parts 1 to 3, Part 6 and Annex B. Those parts state the requirements, the evidence that satisfies each one, and the rules the requirements rest on, quoted from the source named in Annex B with the date each was opened.

**The data-acquisition lead** reads Part 4 (the supplier questionnaire) and Part 5 (the scoring sheet). Those two parts are the operational instrument: send the questionnaire to a supplier, score the answers, and keep the sheet with the contract file.

**The evaluation lead** reads Requirement 8 and the sampling language in Requirement 3.

**Engineering and procurement systems** use Annex A: a machine-readable schema for the supplier's declaration, with an example and a validator, so the declaration can be requested, stored and checked by a tool rather than read from a PDF.

Nothing here is legal advice. The rules are quoted so that counsel can read them in the original; the requirements are written in the form of an assessment procedure: stated scope, stated sampling, evidence that someone outside the transaction can check.

**Conflict disclosure.** The author expects to perform attestation work of the kind Requirement 4 describes through a practice of his own, described in Part 6, and states its rules there; he is also building other businesses in this market, whose work Part 6, rule 3 bars the practice from attesting. Requirement 4 is met by any independent party, including existing audit and assurance firms; no attester receives preference under this document, and the author's own practice is subject to Part 5 like any other.

## 1. Purpose and scope

**Purpose.** To give a buyer of training data a fixed set of questions, a fixed evidence package and a scoring method that make the diligence on a supplier repeatable across suppliers and checkable by someone who did not take part in the purchase.

**Scope.** Any acquisition of data for training, fine-tuning, evaluation or environment construction from a party outside the buyer: a data owner selling its own records, a broker or marketplace, a de-identification or redaction provider delivering a processed corpus, a collector of recorded footage or calls, or a vendor of tasks and traces. It covers text, images, documents, structured records, audio, video and derived artifacts such as reinforcement-learning tasks.

**Out of scope.** The buyer's own internal data; the buyer's model training practices; any statement about a particular supplier, buyer or dataset. The document says what a buyer should ask, what evidence should arrive, and how to score what arrived, and leaves the judgment about any given dataset to the buyer.

**Why the questions are fixed.** A supplier answers the same questions for every buyer, so the answers can be compared; a buyer asks the same questions of every supplier, so a missing answer is visible as a missing answer rather than as a difference in style.

## 2. The record this rests on

Five kinds of rule and standard are the record this document rests on: United States court rules, regulations and statutes, and the standards of ISO/IEC, the IETF and the PCI Security Standards Council; each is quoted or cited in Annex B from its publisher, with the date it was opened.

1. **Evidence rules.** Federal Rule of Evidence 902(13) and (14) make certain electronic records and copied data self-authenticating when a qualified person certifies them and the other side is given notice. A delivery that arrives with a hash manifest and a certification by a qualified person is in the form Rule 902(13) and (14) describe; whether the record is self-authenticating, whether it is admissible, and every other question remain for counsel and the court.
2. **De-identification rules.** 45 CFR 164.514 defines when health information is not individually identifiable, and offers two methods: an expert determination by a person with appropriate knowledge and experience who documents the methods and results, or the removal of a listed set of identifiers with no actual knowledge that the remainder could identify someone. The expert-determination structure, a named person applying stated methods and documenting the result, is the model this document uses for every de-identification claim, whether or not the data is health data.
3. **Independence rules.** 17 CFR 210.2-01 states the standard under which the Securities and Exchange Commission recognizes an accountant as independent, and treats a contingent fee, a fee that depends on a finding or result, as inconsistent with independence. ISO/IEC 17021-1:2015 requires a certification body to be impartial (clauses 5.2.1 and 5.3.2). These are rules that auditors of SEC registrants and management-system certification bodies work under, and they are the model for any attestation a supplier offers.
4. **Timestamp standards.** RFC 3161 defines a time-stamp token issued by a third-party authority that evidences, on trust in that authority, that a hash existed before the time stated. For context only, since no requirement in v0 depends on it: Certificate Transparency (RFC 6962, the version deployed on the public web, and RFC 9162, its Experimental successor) is the precedent for an append-only public log that anyone can audit.

5. **Financial-data rules.** PCI DSS v4.0.1 defines account data (the primary account number, cardholder name, expiration date and service code, and the sensitive authentication data: full track data, card verification code, PINs and PIN blocks), forbids storing sensitive authentication data after authorization even if encrypted (issuers excepted under 3.3.3), and names the four approaches that render a stored primary account number unreadable. 15 U.S.C. 6802 conditions a financial institution's disclosure of nonpublic personal information to a nonaffiliated third party on notice and an opportunity to opt out, with stated exceptions. 15 U.S.C. 1681b lists the circumstances under which a consumer reporting agency may furnish a consumer report "and no other". A delivery that contains or derives from any of these classes is answerable in their vocabulary: which class, what was removed or rendered unreadable and how, and under which notice, exception or purpose the data left the institution that held it.

**Why now.** In 2026 a federal court granted final approval of a class settlement over books downloaded from two shadow libraries for use as training data, with the figures on the docket (Annex B.6). Final judgment has been entered in the district court; appeals are pending. Whatever the outcome on appeal, the diligence questions a buyer can answer before a purchase are the ones this document fixes.

## 3. Requirements

Each requirement states what the buyer requires, the evidence that satisfies it, the rule it rests on, and the three tiers at which a supplier can meet it. The tiers are the heart of the method:

- **Declared (D):** the supplier states the answer in writing, in the declaration (Annex A), and the statement is attributable to a named person at the supplier.
- **Measured (M):** the answer is backed by a measurement, made by the supplier or verified by the buyer: method, sample, date, who ran it, and what was left over.
- **Independently attested (A):** a party independent of the supplier, of any de-identification provider, and of any broker or marketplace in the transaction, under a fee fixed before the result was known, attests the measurement and signs it.

"Not measured" and "unknown" are admissible answers at tier D. A supplier that discloses what it did not do has met the declared tier for that requirement; a supplier that asserts what it did not measure has met no tier. The scoring sheet rewards disclosure and penalizes assertion.

### R1 · Provenance and chain of custody

**Requirement.** The supplier states where each component of the delivery came from, how it was collected, who held it between collection and delivery, and under what authority. The delivery is identified by a hash manifest: a cryptographic hash of every file delivered and of the manifest itself, with the hash algorithm named.

**Evidence.** The hash manifest (SHA-256 or stronger); a provenance statement per source; for any component collected from a third party, the agreement or terms under which it was collected; a third-party time-stamp token (RFC 3161) over the manifest hash, which evidences the manifest's content and date from before any dispute.

**Rule basis.** FRE 902(14) (in summary; quoted in B.1): data copied from a device, medium or file is self-authenticating if authenticated by a process of digital identification, when a qualified person provides the certification Rule 902(11) or (12) describes and the notice requirement is met. The manifest is the process, and the certification the qualified person's certification, that the rule names; whether they satisfy it is for counsel and the court.

**Tiers.** D: the statement and the manifest. M: the manifest verified by the buyer against the delivery, and the time-stamp token verified. A: the manifest, token and provenance statement attested by an independent party.

### R2 · Rights and consent basis

**Requirement.** For each component, the supplier states the right under which it may be licensed for training (ownership, license, consent, public-domain status, or a statutory basis), the terms that travel with it (field-of-use limits, attribution, sublicensing, term), and the mechanism by which an individual or rights holder can exclude their material.

**Evidence.** The rights statement per component; copies of licenses or consent language; the exclusion mechanism and its service level; a log of exclusion requests received and honored, in aggregate.

**Rule basis.** The settlement record (Part 2 and Annex B.6). This document requires that the basis be stated so that counsel can evaluate it, and takes no position on any copyright question.

**Tiers.** D: the statements. M: the exclusion log produced from the supplier's system, with counts and dates. A: the statements and the log attested by an independent party who sampled the records.

### R3 · De-identification, stated as a measurement

**Requirement.** Where the delivery is described as de-identified, anonymized, redacted or scrubbed, the supplier states the claim as a measurement: the attacker the de-identification assumes (what outside information and what access the attacker is taken to have), the method, the sample it was measured on and how the sample was chosen, the date, the person who ran it, and what was left over (the residual: records or fields that the method does not cover or did not clear). A claim of complete anonymization, or of a zero residual, is scored as an assertion at every tier; a determination of very small risk under 164.514(b)(1) states a residual and is scored on its documentation.

**Evidence.** The declaration fields in Annex A (attacker assumed, method, sample, residual); the measurement record; for health data, the expert-determination documentation or the safe-harbor identifier list and the actual-knowledge statement.

**Rule basis.** 45 CFR 164.514(b)(1) (in summary; quoted in B.2): a person with appropriate knowledge and experience applies generally accepted principles and methods, determines that the risk is very small that the information could be used, alone or in combination with other reasonably available information, by an anticipated recipient to identify an individual, and documents the methods and results. The document uses this structure for all data: a named person, a stated method, a stated recipient or attacker, and documented results.

**Sampling language for the evaluation lead.** A measurement on a sample the supplier chose after seeing the buyer's questions is weaker than a measurement on a sample drawn by a procedure the supplier could not predict. The declaration records who drew the sample and when relative to the buyer's questions.

**Tiers.** D: the declaration fields stated (attacker assumed, method, sample, date, person, residual), with "not measured" and "unknown" permitted. M: the measurement record attached, or the measurement verified by the buyer. A: the measurement reproduced or verified by an independent party on a sample that party drew.

### R4 · Independence of any attestation offered

**Requirement.** Any attestation, audit, certification or verification that the supplier offers in support of R1 to R3 must come from a party that is independent of the supplier, of any de-identification or redaction provider in the transaction, and of any broker or marketplace that sells or lists the data; and that party's fee must be fixed before the result is known and must not depend on the finding, the sale or the price.

**Evidence.** The attester's identity and its disclosed relationships with every party in the transaction; the fee arrangement in a form that shows it was fixed before the work and is independent of the result; prior engagements between the attester and any party, disclosed.

**Rule basis.** 17 CFR 210.2-01(b) (in summary; quoted in B.3): an accountant is not independent if a reasonable investor with knowledge of all the facts would conclude that the accountant is not capable of exercising objective and impartial judgment; 210.2-01(c)(5): an accountant is not independent if it provides any service for a contingent fee or receives one from the client; 210.2-01(f)(10): a contingent fee is any fee whose amount depends on the finding or result. ISO/IEC 17021-1:2015, clauses 5.2.1 and 5.3.2: impartiality is required of a certification body. These rules are quoted or cited in Annex B.

**Tiers.** Met or not met. When no attestation is offered, R4 is not applicable and is excluded from the total. When an attestation is offered and is independent under the rule above, R4 is met. When it is offered and is not independent, R4 is not met and the attestation is disregarded for R1 to R3, which are then scored on the supplier's own evidence.

### R5 · The evidence package

**Requirement.** Every delivery arrives with a package that a person outside the transaction can check without asking the supplier: the hash manifest (R1), the time-stamp token (R1), the declaration (Annex A) completed and signed by a named person, the measurement records (R3), and a certification by a qualified person in the form Rule 902(11) or (12) describes, so that the buyer can later give the notice Rule 902(11) requires.

**Evidence.** The package itself, with each element present and the manifest covering all of them.

**Rule basis.** FRE 902(11) (in summary; quoted in B.1): before the trial or hearing, the proponent must give an adverse party reasonable written notice of the intent to offer the record and must make the record and certification available for inspection, so that the party has a fair opportunity to challenge them. A buyer that assembles the package at purchase holds the record and certification Rule 902(11) names.

**Tiers.** D: the package complete. M: the package verified by the buyer (hashes recomputed, token verified, declaration validated against the schema). A: the package attested by an independent party.

### R6 · Health data

**Requirement.** Where any component contains or is derived from health information, the supplier states which of the two methods in 45 CFR 164.514(b) was applied, and delivers the corresponding documentation: for an expert determination, the documented methods and results and the identity and qualifications of the person who made it; for the safe-harbor method, the list of identifiers removed and the statement that the supplier has no actual knowledge that the remainder could identify an individual.

**Evidence.** The documentation named above. A statement that data is "HIPAA compliant" with neither document is scored as an assertion.

**Rule basis.** 45 CFR 164.514(a), (b)(1) and (b)(2), quoted in Annex B. The rule binds covered entities and their business associates; where the supplier is neither, this document applies its two methods as the model.

**Tiers.** D: the method named and the documentation delivered. M: for an expert determination, its sample and results reproduced by the buyer or a reviewer; for safe harbor, identifier removal verified on a sample. A: the determination or the removal attested by an independent party.

### R7 · Term, renewal and re-measurement

**Requirement.** A declaration and its measurements describe the delivery they accompany. For a feed, a refresh or a license that renews, each delivery carries its own declaration, and the supplier states the interval at which de-identification and rights are re-measured.

**Evidence.** The re-measurement interval in the declaration; a declaration per delivery; the change log between deliveries.

**Rule basis.** The structure of 164.514(b)(1), which ties the determination to the information and the anticipated recipient at the time it is made; a determination does not describe data it never covered.

**Tiers.** D: the interval stated. M: a declaration per delivery with the change log. A: the interval and the per-delivery declarations attested.

### R8 · Evaluation data and contamination

**Requirement.** Where the delivery is intended for evaluation, benchmark construction or held-out testing, the supplier states whether any component has been published, sold or delivered to any other party, and in what form; whether it overlaps with public benchmarks the supplier checked; and how the supplier prevents the component from entering training sets it supplies.

**Evidence.** The distribution statement; the overlap check and its method; the supplier's separation procedure.

**Rule basis.** None in law; this is the evaluation lead's requirement, and the document records it because a benchmark with an unstated distribution history measures nothing reliable.

**Tiers.** D: the statements. M: the overlap check attached. A: the distribution history and overlap check attested.

### R9 · Deletion and downstream propagation

**Requirement.** The supplier states how a deletion or exclusion request received after delivery reaches the buyer, within what time, and in what form, and whether it has a mechanism to receive such requests from the individuals or rights holders concerned.

**Evidence.** The propagation procedure; the request-intake mechanism; an aggregate log of requests propagated.

**Rule basis.** The buyer's own obligations under the deletion regimes that apply to it, which vary by jurisdiction and are for counsel to map; the requirement here is that the supplier's procedure exists and is stated, so that counsel can map it.

**Tiers.** D: the procedure stated. M: the log produced from the supplier's system. A: the procedure and log attested.

### R10 · Disclosure of relationships

**Requirement.** The supplier discloses every relationship among the parties to the transaction: ownership or control links between the supplier, any broker or marketplace, any de-identification or redaction provider, and any attester; referral fees, revenue shares or commissions among them; and prior engagements between the attester and any of them.

**Evidence.** The disclosure statement, signed by a named person.

**Rule basis.** 17 CFR 210.2-01(b) and (c)(5) (Annex B), and ISO/IEC 17021-1:2015 clauses 5.2.1 and 5.3.2, which require impartiality: a relationship that is not disclosed cannot be evaluated.

**Tiers.** One tier: the disclosure is either complete and signed, or the supplier has not met R10.

### R11 · Financial and payment data

**Requirement.** Where any component contains or is derived from payment card account data, nonpublic personal information held by a financial institution, or consumer report information, the supplier states which of the three classes is present and, per class, delivers the following. For account data: a statement that no sensitive authentication data (full track data, card verification code, PINs or PIN blocks) is present in any form, including encrypted or hashed; the approach from PCI DSS 3.5.1 by which any primary account number present was rendered unreadable (one-way hash of the entire PAN, truncation, index token, or strong cryptography), and a statement that no two forms of the same PAN that could be correlated to reconstruct it are present in the delivery; and the attestation of compliance or report on compliance covering the environment the data left, whether the supplier's own or its processor's. For nonpublic personal information from a financial institution: the notice and opt-out basis under 15 U.S.C. 6802(a) and (b)(1), or the exception relied on under 6802(b)(2) or (e), and the institution's agreement that permits the disclosure and the onward use. For consumer report information: the circumstance in 15 U.S.C. 1681b(a) under which it was obtained, the user's certification, and the supplier's statement of how use in the delivery is within that circumstance. The buyer's counsel judges whether the stated basis covers the delivery; this document fixes the question and the evidence and leaves the answer to counsel.

**Evidence.** The documents named above. A statement that data is "PCI compliant", "tokenized" or "anonymized" that arrives without the documents R11 names for its class is scored as an assertion. A delivery described as free of card data with no search for PAN patterns on a sample is scored as an assertion.

**Rule basis.** PCI DSS v4.0.1 (PCI Security Standards Council, June 2024): Table 2 (account data), the sentence on page 5 that a cardholder data environment exists wherever PAN is stored, processed or transmitted, requirements 3.2.1, 3.3.1, 3.4.1 and 3.5.1, and by number and title requirement 4 (transmission over open, public networks) and 12.8 (third-party service provider relationships); quoted in Annex B.7. 15 U.S.C. 6802(a) and (b)(1), Annex B.8. 15 U.S.C. 1681(b) and 1681b(a), Annex B.9. PCI DSS binds the entities in the payment ecosystem through the card brands and the acquirers; where the supplier is not such an entity, this document applies its definitions and its 3.5.1 approaches as the model, as R6 applies 164.514.

**Tiers.** D: the classes present named (or "none", with the search performed to say so) and the documents delivered. M: the absence of sensitive authentication data and the unreadability of PAN verified on a sample by the buyer or a reviewer (pattern search for PAN formats with a Luhn check, for track-data and verification-code field names, and for correlatable forms of the same PAN); the 6802 and 1681b bases checked against the agreements and certifications delivered. A: the verification attested by an independent party under R4.

## 4. The supplier questionnaire

Send to the supplier with the request for proposal or before contract. Each answer is attributable to a named person. "Not measured", "unknown" and "not applicable, because..." are admissible answers; an answer that asserts a result without the evidence the requirement names is recorded as an assertion.

| No. | Question | Req. | Answer format |
|---|---|---|---|
| 1 | List each component of the delivery with its source, collection method, custodians since collection, the authority under which it was collected, and, for any component collected from a third party, the agreement or terms under which it was collected. | R1 | Table per component |
| 2 | Provide the hash manifest for the delivery (algorithm named) and the time-stamp token over the manifest hash. | R1 | Files; manifest hash |
| 3 | For each component, state the right under which it may be licensed for training and the terms that travel with it. | R2 | Table per component |
| 4 | Describe the exclusion mechanism for individuals and rights holders, its service level, and the aggregate count of requests received and honored in the last 12 months. | R2 | Text; counts |
| 5 | Is any part of the delivery described as de-identified, anonymized, redacted or scrubbed? If yes: attacker assumed; method; sample (size, how drawn, by whom, when relative to the buyer's questions); date; person who ran it; residual. | R3 | Declaration fields (Annex A) |
| 6 | Does any attestation, audit or verification accompany the delivery? If yes: attester's identity; its relationships with every party; the fee arrangement and when it was fixed; prior engagements. | R4, R10 | Text; documents |
| 7 | List the elements of the evidence package delivered (manifest, token, declaration, measurement records, certification and notice material). | R5 | Checklist |
| 8 | Does any component contain or derive from health information? If yes: which 164.514(b) method; the documentation named in R6. | R6 | Documents |
| 9 | Is this a one-time delivery or a feed, refresh or renewing license? If the latter: the re-measurement interval, the per-delivery declaration practice, and the change log between deliveries. | R7 | Text; change log |
| 10 | If intended for evaluation: distribution history of each component; overlap checks performed and their method; separation procedure from training supplies. | R8 | Text; records |
| 11 | How does a deletion or exclusion request received after delivery reach the buyer, within what time, in what form? Does a mechanism exist for individuals or rights holders to submit such requests to you? Provide the aggregate count propagated in the last 12 months. | R9 | Text; count |
| 12 | Disclose every ownership, control, fee, revenue-share, commission or prior-engagement relationship among supplier, broker or marketplace, de-identification provider and attester. | R10 | Signed statement |
| 13 | Does any component contain or derive from payment card account data, nonpublic personal information held by a financial institution, or consumer report information? If yes, per class: the statements, the 3.5.1 approach, the attestation of compliance, the 6802 basis and agreement, the 1681b circumstance and certification named in R11. If no: the search performed to say so. | R11 | Documents; search record |
| 14 | Name the person accountable for these answers, their role, and the date. | all | Name; role; date |

From AI Training Data Supplier Diligence v0 (Weeks, 2026), CC BY 4.0. The thresholds, and the judgment on any dataset, are the buyer's; the document contains no legal advice.

## 5. The scoring sheet

One sheet per supplier per delivery. Score each requirement at the tier the evidence supports. The thresholds are the buyer's to set; two suggested thresholds are shown as a starting point.

| Requirement | Tier reached (D, M, A, or none) | Evidence present (yes or no) | Assertion recorded (yes or no) | Notes |
|---|---|---|---|---|
| R1 Provenance and custody | | | | |
| R2 Rights and consent basis | | | | |
| R3 De-identification as a measurement | | | | |
| R4 Independence of attestation | | | | |
| R5 Evidence package | | | | |
| R6 Health data | | | | |
| R7 Term and re-measurement | | | | |
| R8 Evaluation data | | | | |
| R9 Deletion propagation | | | | |
| R10 Disclosure of relationships | | | | |
| R11 Financial and payment data | | | | |
| Total (applicable requirements only) | | | | |
| Thresholds used | | | | |
| Scored by; date | | | | |

**Scoring.** None = 0, D = 1, M = 2, A = 3 per requirement. R4 and R10 are scored met (3) or not met (0). A requirement that does not apply to the delivery is recorded as N/A with the reason and is excluded from the total: R3 when nothing is described as de-identified, R4 when no attestation is offered, R6 when no component contains health information, R7 when the delivery is one-time, R8 when the delivery is not intended for evaluation, R11 when no component contains or derives from any of its three classes and the search that supports that answer is recorded. An assertion recorded against any requirement caps that requirement at 0 until the supplier withdraws it or replaces it with a declaration.

**Suggested thresholds.** For a purchase intended for training a released model: every applicable requirement at D or better, with no answer of "unknown" on R1 or R2; R1 and R5 at M or better; R3 at M or better where it applies; R4 met where it applies; R10 met; R11 at M or better where it applies. For a purchase used in evaluation: additionally R8 at M or better. A buyer may set its own thresholds; the sheet records the thresholds used beside the score.

**What the sheet is for.** Comparison across suppliers on the same questions; a record, kept with the contract, of what was asked, what arrived and what was missing; and a record of the diligence performed, in a form a later reader can check.

From AI Training Data Supplier Diligence v0 (Weeks, 2026), CC BY 4.0. The thresholds, and the judgment on any dataset, are the buyer's; the document contains no legal advice.

## 6. Statement of the author's practice

This section is the independence policy of the practice. In this section, the practice means the author and any entity under his control through which he performs the attestation work Part 0 describes. It is published so that a buyer can score that practice under Part 5 on the same terms as any other attester. Attestation here has the Annex C meaning.

**Rules.** The practice follows these rules on every attestation engagement it accepts:

1. it accepts no attestation engagement where the practice, its owners or its staff hold a financial interest in the sale, the price or the licensing of the data attested;
2. it charges and accepts no fee that depends on the finding, the result, the sale or the price; every fee is fixed before the result is known;
3. it attests no work performed by a business under common ownership or control with the practice, and discloses any affiliated business;
4. it discloses, on every attestation, prior engagements with any party to the transaction;
5. it publishes the method under which each attestation is made, so that a reader can check the method against the result;
6. it states, on every attestation, the attacker assumed, the sample and how it was drawn, the date, the person who signed, and the residual, recorded as found or as unknown;
7. it accepts scoring under Part 5 whenever it supplies an attestation.

**Scope.** The rules apply to attestation engagements the practice accepts under Requirement 4 of this document, from the date of the version in which they appear.

**Exclusions.** The practice is separate from any employer of the author. Nothing in this section describes, binds or is performed through any employer or client of the author, and nothing in it describes any dataset, supplier or buyer.

**Revision and remedy.** A departure from a rule is disclosed on the attestation it affects. A rule is changed, or this section withdrawn, only by a dated revision of this document logged in Part 7 with the reason; a revision applies to engagements accepted after its date.

**Status.** This section is policy. It creates no warranty, no assurance of any result, no legal advice, no promise to any reader, and no right in any third party.

## 7. Versioning, seal and citation

**Version.** v0, 2026-11-16, public draft for adoption. Later versions carry a change log here.

**Seal.** At publication, the SHA-256 of the published PDF and the SHA-256 of the Markdown source are time-stamped by a third-party time-stamp authority under RFC 3161, and the tokens are published beside the document, so that the document's content and date can be verified without the author. The band at the head of the body pages and the square mark on the cover are generated deterministically from the SHA-256 of the Markdown source.

**Change log.** v0: first publication.

**Citation.** Weeks, A. D. (2026). AI Training Data Supplier Diligence: Requirements and Evidence, v0. Sealed on the date in the published time-stamp token. The schema (Annex A) is cited by its `$id` and version.

**License.** Text under Creative Commons Attribution 4.0 International, excluding the quoted material in Annex B, which remains its publishers'; the schema, example and validator under the MIT License; the cover engraving, drawn from the author's own photograph, under the same CC BY 4.0 licence as the text. A buyer may reproduce Parts 4 and 5 in its own procurement documents with attribution.

## Annex A · The supplier declaration, machine-readable

The declaration is a JSON document validated against `supplier-declaration.schema.json` (JSON Schema 2020-12). It carries the answers to Part 4 in fixed fields, so that a procurement system can request it, a supplier can attach it to an offer, and a reviewer can validate it with one command. The schema is free, permissively licensed and versioned by its `$id`; a published version is not changed, and a breaking change is a new version with a new `$id`, so a declaration that validated once validates against that version again; depending on it is a choice.

The field names are the vocabulary of Part 3: `attacker_assumed`, `measured_on`, `residual`, `tier`, `health_data`, `financial_data`. The `financial_data` block carries R11: the classes present, and per class the sensitive-authentication-data statement, the 3.5.1 approach, the compliance evidence hash, the 6802 basis and agreement hash, or the 1681b circumstance and certification hash; `classes` empty requires `search_performed`. The attacker is stated on a fixed scale, this document's convention, so that two suppliers' claims can be compared: `T0-public-only` (an attacker with public information only), `T1-public-plus-one-release` (public information plus one prior release from the same source), `T2-insider-without-keys` (access to the supplier's systems but not to any secret material used in de-identification), `T3-insider-with-other-releases` (an insider holding other releases), `T4-model-access-black-box` (query access to a model trained on the data), `T5-model-access-grey-box` (access to the model's weights or internals), or `none-stated`.

Validate with: `python3 validate.py supplier-declaration.schema.json example-declaration.json`.

The schema, the example and the validator are published beside this document.

## Annex B · The rules, quoted

Each quotation is taken from the source named on the date shown. Where a rule is longer than the quoted part, the omission is marked. Quoted text is reproduced as it appeared at the source on the date opened, including the source's punctuation. The eCFR describes itself as authoritative but not an official legal edition; the Legal Information Institute republishes the Federal Rules of Evidence.

### B.1 Federal Rule of Evidence 902 (Legal Information Institute, Cornell Law School; opened 2026-11-05)

Opening: "The following items of evidence are self-authenticating; they require no extrinsic evidence of authenticity in order to be admitted:"

902(11), notice requirement (part): "Before the trial or hearing, the proponent must give an adverse party reasonable written notice of the intent to offer the record — and must make the record and certification available for inspection — so that the party has a fair opportunity to challenge them."

902(13): "Certified Records Generated by an Electronic Process or System. A record generated by an electronic process or system that produces an accurate result, as shown by a certification of a qualified person that complies with the certification requirements of Rule 902(11) or (12). The proponent must also meet the notice requirements of Rule 902(11)."

902(14): "Certified Data Copied from an Electronic Device, Storage Medium, or File. Data copied from an electronic device, storage medium, or file, if authenticated by a process of digital identification, as shown by a certification of a qualified person that complies with the certification requirements of Rule (902(11) or (12) [sic]. The proponent also must meet the notice requirements of Rule 902 (11)."

### B.2 45 CFR 164.514 (eCFR, current to 2026-10-23; opened 2026-11-05)

164.514(a): "Health information that does not identify an individual and with respect to which there is no reasonable basis to believe that the information can be used to identify an individual is not individually identifiable health information."

164.514(b), introduction and (b)(1): "A covered entity may determine that health information is not individually identifiable health information only if: (1) A person with appropriate knowledge of and experience with generally accepted statistical and scientific principles and methods for rendering information not individually identifiable: (i) Applying such principles and methods, determines that the risk is very small that the information could be used, alone or in combination with other reasonably available information, by an anticipated recipient to identify an individual who is a subject of the information; and (ii) Documents the methods and results of the analysis that justify such determination; or"

164.514(b)(2)(i), introduction: "The following identifiers of the individual or of relatives, employers, or household members of the individual, are removed:" (the list of identifiers follows in the rule)

164.514(b)(2)(ii): "The covered entity does not have actual knowledge that the information could be used alone or in combination with other information to identify an individual who is a subject of the information."

### B.3 17 CFR 210.2-01 (eCFR, current to 2026-10-23; opened 2026-11-05)

210.2-01(b): "The Commission will not recognize an accountant as independent, with respect to an audit client, if the accountant is not, or a reasonable investor with knowledge of all relevant facts and circumstances would conclude that the accountant is not, capable of exercising objective and impartial judgment on all issues encompassed within the accountant's engagement."

210.2-01(c)(5), Contingent fees: "An accountant is not independent if, at any point during the audit and professional engagement period, the accountant provides any service or product to an audit client for a contingent fee or a commission, or receives a contingent fee or commission from an audit client."

210.2-01(f)(10): "Contingent fee means, except as stated in the next sentence, any fee established for the sale of a product or the performance of any service pursuant to an arrangement in which no fee will be charged unless a specified finding or result is attained, or in which the amount of the fee is otherwise dependent upon the finding or result of such product or service. Solely for the purposes of this section, a fee is not a “contingent fee” if it is fixed by courts or other public authorities, or, in tax matters, if determined based on the results of judicial proceedings or the findings of governmental agencies. Fees may vary depending, for example, on the complexity of services rendered."

### B.4 ISO/IEC 17021-1:2015

Conformity assessment. Requirements for bodies providing audit and certification of management systems. Part 1: Requirements. Clauses 5.2.1 and 5.3.2 require impartiality of a certification body. The standard's text is copyrighted by ISO and is not reproduced; the clauses are cited for counsel to read in the licensed copy.

### B.5 RFC 3161 and RFC 9162 (RFC Editor; opened 2026-11-05)

RFC 3161, Internet X.509 Public Key Infrastructure Time-Stamp Protocol (TSP), C. Adams, P. Cain, D. Pinkas, R. Zuccherato, August 2001, Proposed Standard, updated by RFC 5816. The document "describes the format of a request sent to a Time Stamping Authority (TSA) and of the response that is returned" and "establishes several security-relevant requirements for TSA operation".

RFC 6962, Certificate Transparency, is the version deployed on the public web. RFC 9162, Certificate Transparency Version 2.0, B. Laurie, E. Messeri, R. Stradling, December 2021, Experimental; obsoletes RFC 6962. It "describes version 2.0 of the Certificate Transparency (CT) protocol for publicly logging the existence of Transport Layer Security (TLS) server certificates as they are issued or observed, in a manner that allows anyone to audit certification authority (CA) activity". Logs are "network services that implement the protocol operations for submissions and queries".

### B.6 Bartz v. Anthropic PBC (N.D. Cal. No. 3:24-cv-05417; docket opened 2026-11-05)

Bartz v. Anthropic PBC, N.D. Cal. No. 3:24-cv-05417-AMO. Order Granting Final Approval of Class Action Settlement, Dkt. 680, filed July 20, 2026 (Martinez-Olguin, J.); the class comprises owners of the exclusive right to reproduce books in the versions of two shadow libraries downloaded by the defendant, as listed on the Works List: "The non-reversionary Settlement Fund of $1.5 billion provides meaningful relief to the Settlement Class" (part; the sentence continues); "The estimated per-work payment of approximately $3,000 is four times the minimum statutory damages amount for willful infringement"; as of April 16, 2026, "91.3 percent of the Works List had been claimed, for a total of 440,490 works of the 482,460 Works on the Works List." Notices of appeal to the Ninth Circuit include Dkt. 682 and 683 (August 2026; Ninth Circuit Nos. 26-5391 and 26-5455); the appeals are pending.

### B.7 PCI DSS v4.0.1 (PCI Security Standards Council, June 2024; the standard as published, opened 2026-11-05)

Page 4, Table 2, Account Data: "Cardholder Data includes: Primary Account Number (PAN); Cardholder Name; Expiration Date; Service Code". "Sensitive Authentication Data includes: Full track data (magnetic-stripe data or equivalent on a chip); Card verification code; PINs/PIN blocks".

Page 5: "If an entity stores, processes, or transmits PAN, then a CDE exists to which PCI DSS requirements will apply."

Requirement 3.2.1, opening: "Account data storage is kept to a minimum through implementation of data retention and disposal policies, procedures, and processes".

Requirement 3.3.1: "SAD is not stored after authorization, even if encrypted. All sensitive authentication data received is rendered unrecoverable upon completion of the authorization process."

Requirement 3.4.1, opening: "PAN is masked when displayed (the BIN and last four digits are the maximum number of digits to be displayed), such that only personnel with a legitimate business need can see more than the BIN and last four digits of the PAN."

Requirement 3.5.1: "PAN is rendered unreadable anywhere it is stored by using any of the following approaches:" "One-way hashes based on strong cryptography of the entire PAN." "Truncation (hashing cannot be used to replace the truncated segment of PAN)." "If hashed and truncated versions of the same PAN, or different truncation formats of the same PAN, are present in an environment, additional controls are in place such that the different versions cannot be correlated to reconstruct the original PAN." "Index tokens." "Strong cryptography with associated key-management processes and procedures."

Requirement 4, titled "Protect Cardholder Data with Strong Cryptography During Transmission Over Open, Public Networks", and requirement 12.8, "Risk to information assets associated with third-party service provider (TPSP) relationships is managed.", are cited by number and title; their sub-requirements are not reproduced here.

### B.8 15 U.S.C. 6802 (Legal Information Institute, Cornell Law School; opened 2026-11-05)

6802(a): "Except as otherwise provided in this subchapter, a financial institution may not, directly or through any affiliate, disclose to a nonaffiliated third party any nonpublic personal information, unless such financial institution provides or has provided to the consumer a notice that complies with section 6803 of this title."

6802(b)(1): "A financial institution may not disclose nonpublic personal information to a nonaffiliated third party unless— (A) such financial institution clearly and conspicuously discloses to the consumer, in writing or in electronic form or other form permitted by the regulations prescribed under section 6804 of this title, that such information may be disclosed to such third party; (B) the consumer is given the opportunity, before the time that such information is initially disclosed, to direct that such information not be disclosed to such third party; and (C) the consumer is given an explanation of how the consumer can exercise that nondisclosure option."

6802(b)(2) (the service-provider exception) and 6802(e) (the general exceptions, including disclosure "with the consent or at the direction of the consumer") are cited by subsection; their text is not reproduced here.

### B.9 15 U.S.C. 1681 and 1681b (Legal Information Institute, Cornell Law School; opened 2026-11-05)

1681(b): "It is the purpose of this subchapter to require that consumer reporting agencies adopt reasonable procedures for meeting the needs of commerce for consumer credit, personnel, insurance, and other information in a manner which is fair and equitable to the consumer, with regard to the confidentiality, accuracy, relevancy, and proper utilization of such information in accordance with the requirements of this subchapter."

1681b(a), opening: "Subject to subsection (c), any consumer reporting agency may furnish a consumer report under the following circumstances and no other:"

1681b(a)(3), lead-in and (A): "To a person which it has reason to believe— (A) intends to use the information in connection with a credit transaction involving the consumer on whom the information is to be furnished and involving the extension of credit to, or review or collection of an account of, the consumer; or"

1681b(a)(3)(F): "otherwise has a legitimate business need for the information— (i) in connection with a business transaction that is initiated by the consumer; or (ii) to review an account to determine whether the consumer continues to meet the terms of the account."

## Annex C · Glossary

**Assertion.** A claim of a result without the evidence the requirement names. Scored at zero.

**Attacker assumed.** The outside information and access a de-identification measurement takes the adversary to have, on the T0 to T5 scale in Annex A.

**Attestation.** A signed statement by a named person at an independent party that a measurement was made as described and produced the stated result. The word is used in this sense throughout. It does not refer to an attest engagement under any accountancy statute or AICPA standard; a PCI DSS attestation of compliance is named as such where it is meant.

**Declaration.** The supplier's own signed statement of the answers to Part 4, in the Annex A format.

**Evidence package.** The manifest, token, declaration, measurement records and certification and notice material that accompany a delivery (R5).

**Hash manifest.** A list of every delivered file with its cryptographic hash, and the hash of the list itself.

**Independent.** Meeting the standard in R4: independent of the supplier, of any de-identification or redaction provider in the transaction, and of any broker or marketplace that sells or lists the data, under a fee fixed before the result is known.

**Measurement.** A method applied to a stated sample on a stated date by a named person, with a stated residual.

**Residual.** What a measurement found left over: records, fields or cases the method does not cover or did not clear.

**Tier.** The level at which a requirement is met: none, declared, measured, independently attested; or not applicable.

**Time-stamp token.** A third-party authority's statement under RFC 3161 that a given hash existed before the time stated, on trust in that authority.
