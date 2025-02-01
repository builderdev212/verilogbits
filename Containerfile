# Setup dependancy versions
ARG DEBIAN_VERSION=12-slim
 
FROM docker.io/library/debian:${DEBIAN_VERSION}
 
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y \
    python3.11 \
    python3-pip \
    python3-venv \
    autoconf gperf make gcc g++ bison flex \
    git help2man perl perl-doc \
    libfl2 libfl-dev \
    ccache mold libgoogle-perftools-dev numactl \
    zlib1g zlib1g-dev \
    gtkwave

# Setup verilator
WORKDIR /usr/src/
ENV VERILATOR_VERSION=5.020
RUN git clone https://github.com/verilator/verilator.git
WORKDIR /usr/src/verilator
RUN git checkout v${VERILATOR_VERSION}
RUN autoconf && ./configure && make -j `nproc` && make install
WORKDIR /usr/src/

# setup python virtual environment
ENV VIRTUAL_ENV=.venv
RUN python3 -m venv ${VIRTUAL_ENV}
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

RUN pip3 install wheel
# install needed python libraries
COPY requirements.txt .
RUN pip3 install -r requirements.txt && \
    rm requirements.txt
 
# jank way to activate the virtual environment
ENTRYPOINT . .venv/bin/activate && /bin/bash
