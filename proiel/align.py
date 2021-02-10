#!/usr/bin/env python3

data = {}

for line in open("greek-nt.tsv"):
    div_id, sentence_id, token_id, citation, form, morphology, pos, lemma = line.strip().split("\t")

    data[token_id] = {
        "div_id": div_id,
        "sentence_id": sentence_id,
        "citation": citation,
        "form": form,
        "morphology": morphology,
        "pos": pos,
        "lemma": lemma,
    }


for line in open("gothic-nt.tsv"):
    div_id, sentence_id, token_id, citation, form, morphology, pos, lemma, greek_div_id, greek_token_id = line.strip().split("\t")

    greek_data = data.get(greek_token_id, {})

    if greek_data.get("div_id"):
        assert greek_data.get("div_id") == greek_div_id

    if greek_data.get("citation"):
        assert greek_data.get("citation") == citation

    print(
        div_id, sentence_id, token_id, citation,
        form, morphology, pos, lemma,
        greek_div_id, greek_token_id,
        greek_data.get("form"),
        greek_data.get("morphology"),
        greek_data.get("pos"),
        greek_data.get("lemma"),
        sep="\t"
    )