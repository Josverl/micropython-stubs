# See here for image contents: https://github.com/devcontainers/images/tree/main/src/python

# [Choice] Python version: 3.14, 3.13, 3.12, 3.11, 3.10 (optionally suffixed with -bookworm or -trixie)
ARG VARIANT="3.14-bookworm"
FROM mcr.microsoft.com/devcontainers/python:${VARIANT}

# The base image includes Yarn, but its APT repository currently uses an expired signing key.
RUN rm -f /etc/apt/sources.list.d/yarn.list

# [Choice] Node.js version: none, lts/*, 16, 14, 12, 10
ARG NODE_VERSION="none"
RUN if [ "${NODE_VERSION}" != "none" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi

# Install development command-line tools for all container users.
RUN curl -LsSf https://astral.sh/uv/install.sh | env UV_UNMANAGED_INSTALL=/usr/local/bin sh \
	&& uv --version

ARG JUST_VERSION="1.58.0"
RUN curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --tag "${JUST_VERSION}" --to /usr/local/bin \
	&& just --version

ARG TARGETARCH
ARG BEADS_VERSION="1.3.0"
RUN set -eux; \
	archive="beads_${BEADS_VERSION}_linux_${TARGETARCH}.tar.gz"; \
	release_url="https://github.com/gastownhall/beads/releases/download/v${BEADS_VERSION}"; \
	curl -fsSL "${release_url}/${archive}" -o "/tmp/${archive}"; \
	curl -fsSL "${release_url}/checksums.txt" -o /tmp/beads-checksums.txt; \
	(cd /tmp && grep " ${archive}$" beads-checksums.txt | sha256sum --check -); \
	mkdir /tmp/beads; \
	tar -xzf "/tmp/${archive}" -C /tmp/beads; \
	find /tmp/beads -type f -name bd -exec install -m 0755 {} /usr/local/bin/bd \;; \
	ln -s bd /usr/local/bin/beads; \
	rm -rf "/tmp/${archive}" /tmp/beads-checksums.txt /tmp/beads; \
	bd version

# [Optional] If your pip requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

# [Optional] Uncomment this line to install global node packages.
# RUN su vscode -c "source /usr/local/share/nvm/nvm.sh && npm install -g <your-package-here>" 2>&1