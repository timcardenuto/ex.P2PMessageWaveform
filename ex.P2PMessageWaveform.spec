# RPM package for ex.P2PMessageWaveform
# This file is regularly AUTO-GENERATED by the IDE. DO NOT MODIFY.

# By default, the RPM will install to the standard REDHAWK SDR root location (/var/redhawk/sdr)
# You can override this at install time using --prefix /new/sdr/root when invoking rpm (preferred method, if you must)
%{!?_sdrroot: %global _sdrroot /var/redhawk/sdr}
%define _prefix %{_sdrroot}
Prefix: %{_prefix}

Name: ex.P2PMessageWaveform
Summary: Waveform ex.P2PMessageWaveform
Version: 1.0.0
Release: 1
License: None
Group: REDHAWK/Waveforms
Source: %{name}-%{version}.tar.gz
# Require the controller whose SPD is referenced
Requires: MessageConsumer
# Require each referenced component
Requires: MessageConsumer MessageProducer
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

%description

%prep
%setup

%install
%__rm -rf $RPM_BUILD_ROOT
%__mkdir_p "$RPM_BUILD_ROOT%{_prefix}/dom/waveforms/ex/P2PMessageWaveform"
%__install -m 644 ex.P2PMessageWaveform.sad.xml $RPM_BUILD_ROOT%{_prefix}/dom/waveforms/ex/P2PMessageWaveform/ex.P2PMessageWaveform.sad.xml

%files
%defattr(-,redhawk,redhawk)
%dir %{_prefix}/dom/waveforms/ex
%dir %{_prefix}/dom/waveforms/ex/P2PMessageWaveform
%{_prefix}/dom/waveforms/ex/P2PMessageWaveform/ex.P2PMessageWaveform.sad.xml
