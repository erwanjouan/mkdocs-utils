const SECRETS_API = "http://127.0.0.1:9371";

function _showToast(message) {
    const toast = document.createElement("div");
    toast.textContent = message;
    Object.assign(toast.style, {
        position: "fixed",
        bottom: "1.5rem",
        left: "50%",
        transform: "translateX(-50%)",
        background: "#323232",
        color: "#fff",
        padding: "0.5rem 1.2rem",
        borderRadius: "4px",
        fontSize: "0.875rem",
        opacity: "1",
        transition: "opacity 0.4s ease",
        zIndex: "9999",
        pointerEvents: "none",
    });
    document.body.appendChild(toast);
    setTimeout(() => { toast.style.opacity = "0"; }, 1800);
    setTimeout(() => { toast.remove(); }, 2200);
}

// key: dot-separated path into the secrets YAML (e.g. "tech-notes.awsaccount2user.mot de passe")
async function copySecret(category, name, property, buttonEl) {
    try {
        const url = `${SECRETS_API}/api/copy?${getParams(category, name, property)}`;
        const res = await fetch(url);
        if (!res.ok) {
            const body = await res.json().catch(() => ({}));
            throw new Error(body.error || `HTTP ${res.status}`);
        }
        _showToast("Copied ✔");
    } catch (err) {
        alert(`[coffre-fort] copySecret failed: ${err.message}`);
        console.error("[secrets] copySecret failed:", err.message);
    }
}

// Returns the value at the given dot-separated key, copies it to clipboard, or throws on error.
async function getAndCopySecret(category, name, property) {
    const url = `${SECRETS_API}/api/get?${getParams(category, name, property)}`;
    const res = await fetch(url);
    const body = await res.json().catch(() => ({}));
    if (!res.ok) throw new Error(body.error || `HTTP ${res.status}`);
    _showToast("Copied ✔");
    return body.value;
}

async function openPage(event, category, name, property) {
    event.preventDefault();
    try {
        url = await getAndCopySecret(category, name, property)
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