# AI Training Data Supplier Diligence

Requirements and Evidence for Buyers of AI Training Data. Version 0 (v0), public draft for adoption, 2026-11-16. Andrew Delaurier Weeks.

The edition is dated 2026-11-16, the UTC date of its seal; this repository was made public on 2026-11-17 (UTC).

Written and published by the author in a personal capacity. No employer or client of the author took part in it, reviewed it, or is bound by it, and no employer of the author has any role in the practice described in Part 6. Reading it forms no engagement and no professional relationship. It is a procurement standard; it contains no legal advice and is no audit, certification or assurance of any result.

## The files

| File | What it is |
|---|---|
| `AI-TDSD-v0.pdf` | The document, 37 pages |
| `AI-TDSD-v0.md` | The Markdown source of the document's text |
| `AI-TDSD-v0.sha256` | The SHA-256 of the PDF and of the source text |
| `AI-TDSD-v0.tsr` | The RFC 3161 time-stamp token over the SHA-256 of the PDF |
| `AI-TDSD-v0.md.tsr` | The RFC 3161 time-stamp token over the SHA-256 of the source text |
| `schema/supplier-declaration.schema.json` | The supplier declaration schema (JSON Schema 2020-12), `urn:aitdsd:supplier-declaration:0.2.0` |
| `schema/example-declaration.json` | An example declaration |
| `schema/validate.py` | The validator |
| `schema/LICENSE` | The MIT License of the schema, the example and the validator |
| `.gitattributes` | Tells Git to keep line ends as stored, so a checkout holds the hashed bytes of the source text |

## Verify the seal

The two tokens were issued by DigiCert's time-stamp authority on 2026-11-16, at 23:17:55 UTC for the PDF and at 23:18:15 UTC for the source text.

Check both files against `AI-TDSD-v0.sha256`:

```
sha256sum -c AI-TDSD-v0.sha256
```

It prints `AI-TDSD-v0.pdf: OK` and `AI-TDSD-v0.md: OK`.

Verify each token against its file. The root certificate is the self-signed DigiCert Trusted Root G4, SHA-256 fingerprint `55:2F:7B:DC:F1:A7:AF:9E:6C:E6:72:01:7F:4F:12:AB:F7:72:40:C7:8E:76:1A:C2:03:D1:D9:D2:0A:C8:99:88`. DigiCert lists this fingerprint and offers a PEM file of the root on its page DigiCert Trusted Root Authority Certificates, https://knowledge.digicert.com/general-information/digicert-trusted-root-authority-certificates (read 2026-11-17). On Debian and Ubuntu the system store holds it at the path shown:

```
openssl ts -verify -data AI-TDSD-v0.pdf -in AI-TDSD-v0.tsr -CAfile /etc/ssl/certs/DigiCert_Trusted_Root_G4.pem
openssl ts -verify -data AI-TDSD-v0.md -in AI-TDSD-v0.md.tsr -CAfile /etc/ssl/certs/DigiCert_Trusted_Root_G4.pem
```

Each command prints `Verification: OK`.

On another system, put in place of that path a PEM file of this root certificate; this command prints the certificate's fingerprint:

```
openssl x509 -in FILE -noout -fingerprint -sha256
```

To read a token's time:

```
openssl ts -reply -in AI-TDSD-v0.tsr -text
```

That printout's `TSA` field reads `unspecified`; the authority is named in the signing certificate inside the token, and this command prints the token's certificates:

```
openssl ts -reply -in AI-TDSD-v0.tsr -token_out | openssl pkcs7 -inform DER -print_certs -noout
```

Among the certificates printed is one named DigiCert Trusted Root G4 and issued by DigiCert Assured ID Root CA. It is a cross-signed certificate for the same key, carried in the token; the verify commands trust the self-signed root with the fingerprint given above.

## Validate a declaration

```
cd schema
pip install jsonschema rfc3339-validator
python3 validate.py supplier-declaration.schema.json example-declaration.json
```

The last command prints `valid: example-declaration.json conforms to AI Training Data Supplier Declaration (AI-TDSD v0) (urn:aitdsd:supplier-declaration:0.2.0)`. The validator exits 0 when the declaration conforms to the schema, 1 with every error listed when it does not, and 2 when it cannot run.

## License

Text under Creative Commons Attribution 4.0 International, excluding the quoted material in Annex B, which remains its publishers'; the schema, example and validator under the MIT License; the cover engraving, drawn from the author's own photograph, under the same CC BY 4.0 licence as the text. A buyer may reproduce Parts 4 and 5 in its own procurement documents with attribution.

## Cite as

Weeks, A. D. (2026). AI Training Data Supplier Diligence: Requirements and Evidence, v0. Sealed on the date in the published time-stamp token. The schema (Annex A) is cited by its `$id` and version.
