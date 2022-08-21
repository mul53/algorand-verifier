(() => {
  function toggleElements(sourceType) {
    const pytealVersionInput = document.getElementById("pyteal-version");
    const pytealModeSelect = document.getElementById("pyteal-mode");
    const sourceUrlInput = document.getElementById("source_url");
    const sourceApprovalUrlInput = document.getElementById(
      "source_approval_url"
    );
    const sourceClearStateUrlInput = document.getElementById(
      "source_clear_state_url"
    );
    const sourceRawText = document.getElementById("source_raw");
    const sourceApprovalText = document.getElementById("source_approval");
    const sourceClearStateText = document.getElementById("source_clear_state");

    if (sourceType === "PT") {
      pytealVersionInput.style.display = "block";
      pytealModeSelect.style.display = "block";
    } else {
      pytealVersionInput.style.display = "none";
      pytealModeSelect.style.display = "none";
    }

    if (sourceType === "TL") {
      sourceUrlInput.style.display = "none";
      sourceApprovalUrlInput.style.display = "block";
      sourceClearStateUrlInput.style.display = "block";

      sourceRawText.style.display = "none";
      sourceApprovalText.style.display = "block";
      sourceClearStateText.style.display = "block";
    } else {
      sourceUrlInput.style.display = "block";
      sourceApprovalUrlInput.style.display = "none";
      sourceClearStateUrlInput.style.display = "none";

      sourceRawText.style.display = "block";
      sourceApprovalText.style.display = "none";
      sourceClearStateText.style.display = "none";
    }
  }

  async function fetchCode(url) {
    const response = await fetch(url);
    return await response.text();
  }

  const sourceTypeSelect = document.getElementById("id_source_type");
  if (!sourceTypeSelect) return;

  sourceTypeSelect.addEventListener("change", (e) => {
    toggleElements(e.target.value);
  });
  toggleElements(sourceTypeSelect.value);

  const sourceUrl = document.getElementById("id_source_url");
  const sourceRaw = document.getElementById("id_source_raw");
  if (!sourceUrl) return;
  sourceUrl.addEventListener("input", async (e) => {
    if (e.target.value) {
      const text = await fetchCode(e.target.value);
      sourceRaw.textContent = text;
    }
  });

  const sourceApprovalUrl = document.getElementById("id_source_approval_url");
  const sourceApproval = document.getElementById("id_source_approval");
  if (!sourceApprovalUrl) return;
  sourceApprovalUrl.addEventListener("input", async (e) => {
    if (e.target.value) {
      const text = await fetchCode(e.target.value);
      sourceApproval.textContent = text;
    }
  });

  const sourceClearStateUrl = document.getElementById(
    "id_source_clear_state_url"
  );
  const sourceClearState = document.getElementById("id_source_clear_state");
  if (!sourceClearStateUrl) return;
  sourceClearStateUrl.addEventListener("input", async (e) => {
    if (e.target.value) {
      const text = await fetchCode(e.target.value);
      sourceClearState.textContent = text;
    }
  });
})();

// Autocomplete component
(() => {
  if (!window.Autocomplete) return;

  new Autocomplete("#autocomplete", {
    search: (input) => {
      const url = `/search?app=${input}`;
      return new Promise((resolve) => {
        fetch(url)
          .then((response) => response.json())
          .then((data) => resolve(data.apps));
      });
    },

    getResultValue: (result) => result.id,

    onSubmit: (result) => {
      location.pathname = `/app/${result.id}`;
    },
  });
})();

// Tabs component
(() => {
  function selectTab(id, predicate) {
    if (!id || !predicate) return;

    document.querySelectorAll(`${id} div`).forEach((e) => {
      if (predicate.includes(e.id)) {
        e.classList.remove("hidden");
      } else {
        e.classList.add("hidden");
      }
    });
  }

  function createTabComponent(el) {
    const tabsToggleId = el.dataset.tabsToggle;
    if (tabsToggleId) {
      el.addEventListener("click", (e) => {
        selectTab(tabsToggleId, e.target.dataset.tabsTarget);
      });

      selectTab(tabsToggleId, el.dataset.tabDefault);
    }
  }

  document.querySelectorAll(".tabs").forEach((el) => createTabComponent(el));
})();
