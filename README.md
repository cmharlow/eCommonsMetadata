#eCommons Metadata Review + RandomScripts

Review of the eCommons DSpace metadata as of Wednesday, February 3rd, 2016.

Total records in the system at that point: 35,193

##Metadata Formats Used by the System:

###dc
This is configured with the DCMI website URL as namespace in platform, not one of the DC schemas namespaces. Seems to get correct namespace in feeds. Includes DC elements and DC terms, as well as some invalid (made up to look like DC) elements.

Fields used (with platform specific use notes where exists):

terms | eCommons def | my notes
--- | --- | ---
dc.contributor.advisor | Use primarily for thesis advisor. |
dc.contributor.author |  |
dc.contributor.chair |  |
dc.contributor.coChair |  |
dc.contributor.committeeMember | |
dc.contributor.editor | |
dc.contributor.illustrator | |
dc.contributor.other | |
dc.contributor | A person, organization, or service responsible for the content of the resource. Catch-all for unspecified contributors. |
dc.coverage.spatial | Spatial characteristics of content. |
dc.coverage.temporal | Temporal characteristics of content. |
dc.creator | Do not use; only for harvested metadata. |
dc.date.accessioned | Date DSpace takes possession of item. |
dc.date.available | Date or date range item became available to the public. |
dc.date.copyright | Date of copyright. |
dc.date.created | Date of creation or manufacture of intellectual content if different from date.issued. |
dc.date.issued | Date of publication or distribution. |
dc.date.submitted | Recommend for theses/dissertations. |
dc.date.updated | The last time the item was updated via the SWORD interface
dc.date | Use qualified form if possible. |
dc.description.abstract | Abstract or summary. |
dc.description.audio | Entry ID for kaltura audio files |
dc.description.embargo | This field controls embargoes for new items |
dc.description.provenance | The history of custody of the item since its creation, including any changes successive custodians made to it. |
dc.description.sponsorship | Information about sponsoring agencies, individuals, or contractual arrangements for the item. |
dc.description.statementofresponsibility | To preserve statement of responsibility from MARC records. |
dc.description.tableofcontents | A table of contents for a given item. |
dc.description.uri | Uniform Resource Identifier pointing to description of this item. |
dc.description.version | The Peer Reviewed status of an item |
dc.description.viewer | Entry ID for Kaltura Viewer |
dc.description | Catch-all for any description not defined by qualifiers. |
dc.format.extent | Size or duration. |
dc.format.medium | Physical medium. |
dc.format.mimetype | Registered MIME type identifiers. |
dc.format | Catch-all for any format information not defined by qualifiers. |
dc.identifier.citation | Human-readable, standard bibliographic citation of non-DSpace format of this item |
dc.identifier.govdoc | A government document number |
dc.identifier.isbn | International Standard Book Number |
dc.identifier.ismn | International Standard Music Number |
dc.identifier.issn | International Standard Serial Number |
dc.identifier.other | A known identifier type common to a local collection. |
dc.identifier.sici | Serial Item and Contribution Identifier |
dc.identifier.slug | a uri supplied via the sword slug header, as a suggested uri for the item |
dc.identifier.uri | Uniform Resource Identifier |
dc.identifier | Catch-all for unambiguous identifiers not defined by qualified form; use identifier.other for a known identifier common to a local collection instead of unqualified form. |
dc.language.iso | Current ISO standard for language of intellectual content, including country codes (e.g. "en_US"). |
dc.language.rfc3066 | the rfc3066 form of the language for the item |
dc.language | Catch-all for non-ISO forms of the language of the item, accommodating harvested values. |
dc.provenance | |
dc.publisher | Entity responsible for publication, distribution, or imprint. |
dc.relation.haspart | References physically or logically contained item. |
dc.relation.hasversion | References later version. |
dc.relation.isbasedon | References source. |
dc.relation.isformatof | References additional physical form. |
dc.relation.ispartof | References physically or logically containing item. |
dc.relation.ispartofseries | Series name and number within that series, if available. |
dc.relation.isreferencedby | Pointed to by referenced resource. |
dc.relation.isreferencedbyuri | URI for Referenced Item |
dc.relation.isreplacedby | References succeeding item. |
dc.relation.isversionof | References earlier version. |
dc.relation.replaces | References preceeding item. |
dc.relation.requires | Referenced resource is required to support function, delivery, or coherence of item. |
dc.relation.uri | References Uniform Resource Identifier for related item. |
dc.relation | Catch-all for references to other related items. |
dc.rights.holder | The owner of the copyright |
dc.rights.license | |
dc.rights.uri | References terms governing use and reproduction. |
dc.rights | Terms governing use and reproduction. |
dc.source.uri | Do not use; only for harvested metadata. |
dc.source | Do not use; only for harvested metadata. |
dc.subject.classification | Catch-all for value from local classification system; global classification systems will receive specific qualifier |
dc.subject.ddc | Dewey Decimal Classification Number |
dc.subject.lcc | Library of Congress Classification Number |
dc.subject.lcsh | Library of Congress Subject Headings |
dc.subject.mesh | MEdical Subject Headings |
dc.subject.other | Local controlled vocabulary; global vocabularies will receive specific qualifier. |
dc.subject | Uncontrolled index term. |
dc.title.alternative | Varying (or substitute) form of title proper appearing in item, e.g. abbreviation or translation |
dc.title | Title statement/title proper. |
dc.type | Nature or genre of content. |

###ETDMS ('ETDSchema', prefix 'thesis:')
Appears to get mapped to DC fields (at least, DC namespace, as most fields aren't valid in DC elements or DC terms) for the discovery layer and OAI feeds.

Namespace: 

Four fields used:

- thesis.degree.discipline
- thesis.degree.grantor
- thesis.degree.level
- thesis.degree.name

In front-facing records, they are shown as is (with thesis prefix).

In the DIM feed, these fields become unmapped text at the end of the <metadata> field (making XML output invalid).

###dcterms
Includes DC elements and DC terms, as well as some invalid (made up to look like DC) elements. Some DCMI Class Names, Date Types, other non-elements used as elements.

Fields used (with platform specific use notes where exists):

terms | eCommons def | my notes
--- | --- | ---
dcterms.abstract | A summary of the resource. |
dcterms.accessRights | Information about who can access the resource or an indication of its security status. May include information regarding access or restrictions based on privacy, security, or other policies. |
dcterms.accrualMethod | The method by which items are added to a collection. |
dcterms.accrualPeriodicity | The frequency with which items are added to a collection. |
dcterms.accrualPolicy | The policy governing the addition of items to a collection. |
dcterms.alternative | An alternative name for the resource. |
dcterms.audience | A class of entity for whom the resource is intended or useful. |
dcterms.available | Date (often a range) that the resource became or will become available. |
dcterms.bibliographicCitation | Recommended practice is to include sufficient bibliographic detail to identify the resource as unambiguously as possible. |
dcterms.comformsTo | An established standard to which the described resource conforms. |
dcterms.contributor | An entity responsible for making contributions to the resource. Examples of a Contributor include a person, an organization, or a service. |
dcterms.coverage | The spatial or temporal topic of the resource, the spatial applicability of the resource, or the jurisdiction under which the resource is relevant. |
dcterms.created | Date of creation of the resource. |
dcterms.creator | An entity primarily responsible for making the resource. |
dcterms.date | A point or period of time associated with an event in the lifecycle of the resource. |
dcterms.dateAccepted | Date of acceptance of the resource. |
dcterms.dateCopyrighted | Date of copyright. |
dcterms.dateSubmitted | Date of submission of the resource. |
dcterms.description | An account of the resource. |
dcterms.educationLevel | A class of entity, defined in terms of progression through an educational or training context, for which the described resource is intended. |
dcterms.extent | The size or duration of the resource. |
dcterms.format | The file format, physical medium, or dimensions of the resource. |
dcterms.hasFormat | A related resource that is substantially the same as the pre-existing described resource, but in another format. |
dcterms.hasPart | A related resource that is included either physically or logically in the described resource. |
dcterms.hasVersion | A related resource that is a version, edition, or adaptation of the described resource. |
dcterms.identifier | An unambiguous reference to the resource within a given context. |
dcterms.instructionalMethod | A process, used to engender knowledge, attitudes and skills, that the described resource is designed to support. |
dcterms.isFormatOf | A related resource that is substantially the same as the described resource, but in another format. |
dcterms.isPartOf | A related resource in which the described resource is physically or logically included. |
dcterms.isReferencedBy | A related resource that references, cites, or otherwise points to the described resource. |
dcterms.isReplacedBy | A related resource that supplants, displaces, or supersedes the described resource. |
dcterms.isRequiredBy | A related resource that requires the described resource to support its function, delivery, or coherence. |
dcterms.issued  Date of formal issuance (e.g., publication) of the resource. |
dcterms.isVersionOf | A related resource of which the described resource is a version, edition, or adaptation. |
dcterms.language | A language of the resource. |
dcterms.license | A legal document giving official permission to do something with the resource. |
dcterms.mediator | An entity that mediates access to the resource and for whom the resource is intended or useful. |
dcterms.medium | The material or physical carrier of the resource. |
dcterms.modified | Date on which the resource was changed. |
dcterms.provenance | A statement of any changes in ownership and custody of the resource since its creation that are significant for its authenticity, integrity, and interpretation. |
dcterms.publisher | An entity responsible for making the resource available.
dcterms.references | A related resource that is referenced, cited, or otherwise pointed to by the described resource. |
dcterms.relation | A related resource. |
dcterms.replaces | A related resource that is supplanted, displaced, or superseded by the described resource. |
dcterms.requires | A related resource that is required by the described resource to support its function, delivery, or coherence. |
dcterms.rights | Information about rights held in and over the resource. |
dcterms.rightsHolder | A person or organization owning or managing rights over the resource. |
dcterms.source | A related resource from which the described resource is derived. |
dcterms.spatial | Spatial characteristics of the resource. |
dcterms.subject | The topic of the resource. |
dcterms.tableOfContents | A list of subunits of the resource. |
dcterms.temporal | Temporal characteristics of the resource. |
dcterms.title | A name given to the resource. |
dcterms.type | The nature or genre of the resource. |
dcterms.valid | Date (often a range) of validity of a resource. |

###eperson (DSpace eperson)

##Metadata Formats as Appear in OAI Feeds:
###OAI_DC
The **oai_dc feed** (which is actually just DC Elements terms) has 35,073 records. Field usage overview in that feed:

```
{http://purl.org/dc/elements/1.1/}contributor: |==                       |   3257/35062 |   9% 
    {http://purl.org/dc/elements/1.1/}creator: |===================      |  27423/35062 |  78% 
       {http://purl.org/dc/elements/1.1/}date: |=========================|  35062/35062 | 100% 
{http://purl.org/dc/elements/1.1/}description: |======================   |  31813/35062 |  90% 
     {http://purl.org/dc/elements/1.1/}format: |=====                    |   7924/35062 |  22% 
 {http://purl.org/dc/elements/1.1/}identifier: |======================== |  35061/35062 |  99% 
   {http://purl.org/dc/elements/1.1/}language: |=======================  |  33243/35062 |  94% 
  {http://purl.org/dc/elements/1.1/}publisher: |=============            |  19376/35062 |  55% 
   {http://purl.org/dc/elements/1.1/}relation: |===                      |   4506/35062 |  12% 
     {http://purl.org/dc/elements/1.1/}rights: |                         |     33/35062 |   0% 
     {http://purl.org/dc/elements/1.1/}source: |                         |      1/35062 |   0% 
    {http://purl.org/dc/elements/1.1/}subject: |====================     |  28617/35062 |  81% 
      {http://purl.org/dc/elements/1.1/}title: |=========================|  35062/35062 | 100% 
       {http://purl.org/dc/elements/1.1/}type: |=======================  |  32972/35062 |  94% 
```


###DIM
The **DIM feed** (DSpace specific schema that mostly replicated awkwardly DC elements and terms) has 35,062 records.

Field usage overview:

```
                          dc:contributor: |                         |      2/35062 |   0% 
                  dc:contributor.advisor: |                         |      5/35062 |   0% 
                   dc:contributor.author: |===================      |  27325/35062 |  77% 
                    dc:contributor.chair: |==                       |   3126/35062 |   8% 
                  dc:contributor.coChair: |                         |    140/35062 |   0% 
          dc:contributor.committeeMember: |==                       |   3116/35062 |   8% 
                   dc:contributor.editor: |                         |    103/35062 |   0% 
                    dc:contributor.other: |                         |     13/35062 |   0% 
                              dc:creator: |                         |     14/35062 |   0% 
                                 dc:date: |                         |     43/35062 |   0% 
                     dc:date.accessioned: |======================== |  35060/35062 |  99% 
                       dc:date.available: |=======================  |  32469/35062 |  92% 
                       dc:date.copyright: |                         |      3/35062 |   0% 
                         dc:date.created: |                         |      1/35062 |   0% 
                          dc:date.issued: |======================== |  34853/35062 |  99% 
                         dc:date.updated: |                         |      1/35062 |   0% 
                          dc:description: |=======                  |  10991/35062 |  31% 
                 dc:description.abstract: |=================        |  24421/35062 |  69% 
                    dc:description.audio: |                         |    201/35062 |   0% 
                  dc:description.embargo: |=                        |   2623/35062 |   7% 
               dc:description.provenance: |======================== |  35031/35062 |  99% 
              dc:description.sponsorship: |                         |   1401/35062 |   3% 
dc:description.statementofresponsibility: |                         |      2/35062 |   0% 
          dc:description.tableofcontents: |                         |      1/35062 |   0% 
                  dc:description.version: |                         |      1/35062 |   0% 
                   dc:description.viewer: |                         |    603/35062 |   1% 
                               dc:format: |                         |     73/35062 |   0% 
                        dc:format.extent: |=====                    |   7846/35062 |  22% 
                        dc:format.medium: |                         |      2/35062 |   0% 
                      dc:format.mimetype: |=====                    |   7848/35062 |  22% 
                           dc:identifier: |                         |      7/35062 |   0% 
                  dc:identifier.citation: |====                     |   5778/35062 |  16% 
                    dc:identifier.govdoc: |                         |      2/35062 |   0% 
                      dc:identifier.isbn: |                         |    102/35062 |   0% 
                      dc:identifier.issn: |                         |    671/35062 |   1% 
                     dc:identifier.other: |==                       |   3091/35062 |   8% 
                       dc:identifier.uri: |======================== |  35060/35062 |  99% 
                             dc:language: |                         |     18/35062 |   0% 
                         dc:language.iso: |=======================  |  33176/35062 |  94% 
                            dc:publisher: |=============            |  19376/35062 |  55% 
                  dc:relation.hasversion: |                         |    249/35062 |   0% 
                   dc:relation.isbasedon: |                         |      1/35062 |   0% 
                    dc:relation.ispartof: |                         |      7/35062 |   0% 
              dc:relation.ispartofseries: |==                       |   4034/35062 |  11% 
              dc:relation.isreferencedby: |                         |      5/35062 |   0% 
           dc:relation.isreferencedbyuri: |                         |      3/35062 |   0% 
                         dc:relation.uri: |                         |    223/35062 |   0% 
                               dc:rights: |                         |     32/35062 |   0% 
                           dc:rights.uri: |                         |     33/35062 |   0% 
                           dc:source.uri: |                         |      1/35062 |   0% 
                              dc:subject: |====================     |  28616/35062 |  81% 
                          dc:subject.ddc: |                         |      3/35062 |   0% 
                        dc:subject.other: |                         |      1/35062 |   0% 
                                dc:title: |=========================|  35062/35062 | 100% 
                    dc:title.alternative: |=                        |   2609/35062 |   7% 
                                 dc:type: |=======================  |  32868/35062 |  93% 
```

###ETDMS 
