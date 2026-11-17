#!/usr/bin/env python3
"""Valida el registro gráfico infantil sin inventar aprobaciones ni asignaciones."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_CODES = ["K-01", "K-02", "K-03", "K-04", "K-05", "K-06", "K-07",
                  "K-08", "K-09", "K-12", "K-14", "K-17", "K-18", "K-23",
                  "K-25", "K-27"]
REQUIRED = ("silhouette", "morphology", "distinctive_marks", "palette",
            "expression_pose", "monochrome_coloring", "source", "state")

def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))

def main():
    cast = load("editorial/elenco_forja_infantil_16.json")
    mapping = load("editorial/asignaciones_karmany_28.json")
    plan = load("editorial/plan_paginas.json")
    characters = cast["creatures"]
    assert [e["code"] for e in characters] == EXPECTED_CODES, "Elenco/códigos alterados"
    assert len({e["name"] for e in characters}) == 16, "Nombres duplicados"
    assert all(e["identity_selected"] for e in characters), "Identidad no seleccionada"
    assert [e["code"] for e in characters if e["visual_approved"]] == EXPECTED_CODES[:4], "Estado de 4 fichas incorrecto"
    for c in characters:
        assert c["pages_assigned"] == [], f"Asignación anticipada en {c['code']}"
        assert all(c["graphic"].get(k) for k in REQUIRED), f"Descripción incompleta: {c['code']}"
        assert c["graphic"]["scope"] == "adaptacion_visual_exclusiva_libro", c["code"]
        if c["visual_approved"]:
            assert c["model_sheet"] and not c["model_sheet"]["asset_in_github"], "No afirmar PNG subido sin verificar"
        else:
            assert c["model_sheet"] is None, "Ficha individual sin aprobación"
    raw_pages = plan if isinstance(plan, list) else plan.get("pages", plan.get("laminas", plan.get("paginas")))
    assert isinstance(raw_pages, list) and len(raw_pages) == 28, "Plan de páginas no contiene 28"
    assert len(mapping["pages"]) == 28, "Matriz no contiene 28"
    for idx, item in enumerate(mapping["pages"]):
        pid = f"P{idx + 1:02d}"
        assert item["page_id"] == raw_pages[idx]["id"] == pid, f"Página incoherente: {pid}"
        assert item["karmany_codes"] == [] and item["assignment_status"] == "sin_asignar", f"Asignación no autorizada: {pid}"
    assert mapping["approved_individual_design_count"] == 4, "Conteo de aprobados incorrecto"
    assert cast["visual_reference"]["asset_in_github"] is False, "Imagen de conjunto sin comprobación"
    print("OK: 16 Karmany descritos, 4 modelos aprobados, 12 pendientes, 28 páginas sin asignar.")

if __name__ == "__main__":
    main()
