from src.app.index.index_handler import create_index
from src.app.llm.llm_handler import set_llm


def get_query_engine():
    query_engine = create_index().as_query_engine(
        llm=set_llm(),
        response_mode="compact")
    return query_engine
