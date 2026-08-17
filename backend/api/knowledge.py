"""
Knowledge Base search + document preview. Powers the Knowledge Base page,
backed by ChromaDB via app/rag/retriever.py.
"""
from fastapi import APIRouter
from backend.rag.retriever import Retriever

router = APIRouter(prefix="/api/knowledge", tags=["knowledge"])


@router.get("/search")
async def search_knowledge_base(q: str, top_k: int = 8):
    retriever = Retriever()
    results = retriever.retrieve(q, k=top_k)
    return {"query": q, "results": results}


@router.get("/document/{doc_id}")
async def get_document(doc_id: str):
    # TODO: fetch full document text/metadata from Chroma by id
    return {"id": doc_id, "content": "TODO: load from vector_store"}
