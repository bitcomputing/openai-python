# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from openai import OpenAI, AsyncOpenAI
from tests.utils import assert_matches_type
from openai.pagination import SyncCursorPage, AsyncCursorPage
from openai.types.beta.threads import (
    Run,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: OpenAI) -> None:
        run = client.beta.threads.runs.create(
            "string",
            assistant_id="string",
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: OpenAI) -> None:
        run = client.beta.threads.runs.create(
            "string",
            assistant_id="string",
            additional_instructions="string",
            instructions="string",
            metadata={},
            model="string",
            tools=[{"type": "code_interpreter"}, {"type": "code_interpreter"}, {"type": "code_interpreter"}],
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: OpenAI) -> None:
        response = client.beta.threads.runs.with_raw_response.create(
            "string",
            assistant_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: OpenAI) -> None:
        with client.beta.threads.runs.with_streaming_response.create(
            "string",
            assistant_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.runs.with_raw_response.create(
                "",
                assistant_id="string",
            )

    @parametrize
    def test_method_retrieve(self, client: OpenAI) -> None:
        run = client.beta.threads.runs.retrieve(
            "string",
            thread_id="string",
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: OpenAI) -> None:
        response = client.beta.threads.runs.with_raw_response.retrieve(
            "string",
            thread_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: OpenAI) -> None:
        with client.beta.threads.runs.with_streaming_response.retrieve(
            "string",
            thread_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.runs.with_raw_response.retrieve(
                "string",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.beta.threads.runs.with_raw_response.retrieve(
                "",
                thread_id="string",
            )

    @parametrize
    def test_method_update(self, client: OpenAI) -> None:
        run = client.beta.threads.runs.update(
            "string",
            thread_id="string",
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: OpenAI) -> None:
        run = client.beta.threads.runs.update(
            "string",
            thread_id="string",
            metadata={},
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: OpenAI) -> None:
        response = client.beta.threads.runs.with_raw_response.update(
            "string",
            thread_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: OpenAI) -> None:
        with client.beta.threads.runs.with_streaming_response.update(
            "string",
            thread_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.runs.with_raw_response.update(
                "string",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.beta.threads.runs.with_raw_response.update(
                "",
                thread_id="string",
            )

    @parametrize
    def test_method_list(self, client: OpenAI) -> None:
        run = client.beta.threads.runs.list(
            "string",
        )
        assert_matches_type(SyncCursorPage[Run], run, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: OpenAI) -> None:
        run = client.beta.threads.runs.list(
            "string",
            after="string",
            before="string",
            limit=0,
            order="asc",
        )
        assert_matches_type(SyncCursorPage[Run], run, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: OpenAI) -> None:
        response = client.beta.threads.runs.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(SyncCursorPage[Run], run, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: OpenAI) -> None:
        with client.beta.threads.runs.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(SyncCursorPage[Run], run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.runs.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_cancel(self, client: OpenAI) -> None:
        run = client.beta.threads.runs.cancel(
            "string",
            thread_id="string",
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: OpenAI) -> None:
        response = client.beta.threads.runs.with_raw_response.cancel(
            "string",
            thread_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: OpenAI) -> None:
        with client.beta.threads.runs.with_streaming_response.cancel(
            "string",
            thread_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.runs.with_raw_response.cancel(
                "string",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.beta.threads.runs.with_raw_response.cancel(
                "",
                thread_id="string",
            )

    @parametrize
    def test_method_submit_tool_outputs(self, client: OpenAI) -> None:
        run = client.beta.threads.runs.submit_tool_outputs(
            "string",
            thread_id="string",
            tool_outputs=[{}, {}, {}],
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    def test_raw_response_submit_tool_outputs(self, client: OpenAI) -> None:
        response = client.beta.threads.runs.with_raw_response.submit_tool_outputs(
            "string",
            thread_id="string",
            tool_outputs=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    def test_streaming_response_submit_tool_outputs(self, client: OpenAI) -> None:
        with client.beta.threads.runs.with_streaming_response.submit_tool_outputs(
            "string",
            thread_id="string",
            tool_outputs=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_submit_tool_outputs(self, client: OpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            client.beta.threads.runs.with_raw_response.submit_tool_outputs(
                "string",
                thread_id="",
                tool_outputs=[{}, {}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.beta.threads.runs.with_raw_response.submit_tool_outputs(
                "",
                thread_id="string",
                tool_outputs=[{}, {}, {}],
            )


class TestAsyncRuns:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOpenAI) -> None:
        run = await async_client.beta.threads.runs.create(
            "string",
            assistant_id="string",
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpenAI) -> None:
        run = await async_client.beta.threads.runs.create(
            "string",
            assistant_id="string",
            additional_instructions="string",
            instructions="string",
            metadata={},
            model="string",
            tools=[{"type": "code_interpreter"}, {"type": "code_interpreter"}, {"type": "code_interpreter"}],
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.threads.runs.with_raw_response.create(
            "string",
            assistant_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.threads.runs.with_streaming_response.create(
            "string",
            assistant_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.runs.with_raw_response.create(
                "",
                assistant_id="string",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOpenAI) -> None:
        run = await async_client.beta.threads.runs.retrieve(
            "string",
            thread_id="string",
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.threads.runs.with_raw_response.retrieve(
            "string",
            thread_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.threads.runs.with_streaming_response.retrieve(
            "string",
            thread_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.runs.with_raw_response.retrieve(
                "string",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.beta.threads.runs.with_raw_response.retrieve(
                "",
                thread_id="string",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncOpenAI) -> None:
        run = await async_client.beta.threads.runs.update(
            "string",
            thread_id="string",
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOpenAI) -> None:
        run = await async_client.beta.threads.runs.update(
            "string",
            thread_id="string",
            metadata={},
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.threads.runs.with_raw_response.update(
            "string",
            thread_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.threads.runs.with_streaming_response.update(
            "string",
            thread_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.runs.with_raw_response.update(
                "string",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.beta.threads.runs.with_raw_response.update(
                "",
                thread_id="string",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOpenAI) -> None:
        run = await async_client.beta.threads.runs.list(
            "string",
        )
        assert_matches_type(AsyncCursorPage[Run], run, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpenAI) -> None:
        run = await async_client.beta.threads.runs.list(
            "string",
            after="string",
            before="string",
            limit=0,
            order="asc",
        )
        assert_matches_type(AsyncCursorPage[Run], run, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.threads.runs.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(AsyncCursorPage[Run], run, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.threads.runs.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(AsyncCursorPage[Run], run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.runs.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncOpenAI) -> None:
        run = await async_client.beta.threads.runs.cancel(
            "string",
            thread_id="string",
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.threads.runs.with_raw_response.cancel(
            "string",
            thread_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.threads.runs.with_streaming_response.cancel(
            "string",
            thread_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.runs.with_raw_response.cancel(
                "string",
                thread_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.beta.threads.runs.with_raw_response.cancel(
                "",
                thread_id="string",
            )

    @parametrize
    async def test_method_submit_tool_outputs(self, async_client: AsyncOpenAI) -> None:
        run = await async_client.beta.threads.runs.submit_tool_outputs(
            "string",
            thread_id="string",
            tool_outputs=[{}, {}, {}],
        )
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    async def test_raw_response_submit_tool_outputs(self, async_client: AsyncOpenAI) -> None:
        response = await async_client.beta.threads.runs.with_raw_response.submit_tool_outputs(
            "string",
            thread_id="string",
            tool_outputs=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Run, run, path=["response"])

    @parametrize
    async def test_streaming_response_submit_tool_outputs(self, async_client: AsyncOpenAI) -> None:
        async with async_client.beta.threads.runs.with_streaming_response.submit_tool_outputs(
            "string",
            thread_id="string",
            tool_outputs=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(Run, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_submit_tool_outputs(self, async_client: AsyncOpenAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `thread_id` but received ''"):
            await async_client.beta.threads.runs.with_raw_response.submit_tool_outputs(
                "string",
                thread_id="",
                tool_outputs=[{}, {}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.beta.threads.runs.with_raw_response.submit_tool_outputs(
                "",
                thread_id="string",
                tool_outputs=[{}, {}, {}],
            )
