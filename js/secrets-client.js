const SECRETS_API = "http://127.0.0.1:9371";

// key: dot-separated path into the secrets YAML (e.g. "tech-notes.awsaccount2user.mot de passe")
async function copySecret(category, name, property, buttonEl) {
    const original = buttonEl ? buttonEl.textContent : null;
    const setLabel = (label) => {
        if (buttonEl) {
            buttonEl.textContent = label;
            setTimeout(() => {
                buttonEl.textContent = original;
            }, 2000);
        }
    };

    try {
        const url = `${SECRETS_API}/api/copy?${getParams(category, name, property)}`;
        const res = await fetch(url);
        if (!res.ok) {
            const body = await res.json().catch(() => ({}));
            throw new Error(body.error || `HTTP ${res.status}`);
        }
        setLabel("copied ✔");
    } catch (err) {
        alert(`[coffre-fort] copySecret failed: ${err.message}`);
        console.error("[secrets] copySecret failed:", err.message);
        setLabel("Error");
    }
}

// Returns the value at the given dot-separated key, or throws on error.
async function getSecret(category, name, property) {
    const url = `${SECRETS_API}/api/get?${getParams(category, name, property)}`;
    const res = await fetch(url);
    const body = await res.json().catch(() => ({}));
    if (!res.ok) throw new Error(body.error || `HTTP ${res.status}`);
    return body.value;
}

async function openPage(event, category, name, property) {
    event.preventDefault();
    try {
        url = await getSecret(category, name, property)
        if (url) {
            window.open(url, '_blank');
        }
    } catch (err) {
        alert(`[coffre-fort] openPage failed: ${err.message}`);
        console.error("[secrets] openPage failed:", err.message);
    }
}

function getParams(category, name, property) {
    const categoryParam = `category=${encodeURIComponent(category)}`
    const keyParam = `name=${encodeURIComponent(name)}`
    const propertyParam = `property=${encodeURIComponent(property)}`
    return `${categoryParam}&${keyParam}&${propertyParam}`
}